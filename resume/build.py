#!/usr/bin/env python3
"""
build.py -- render the CV from YAML + BibTeX into a single cv.tex.

Inputs:
  data/*.yaml          one YAML file per section
  publications.bib     master bibliography
  templates/cv.tex.j2  master Jinja2 template
  templates/partials/  per-section Jinja2 partials

Output:
  cv.tex               concatenated LaTeX source (do not hand-edit)

Run:
  python3 build.py
  # then: latexmk -pdf cv.tex
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

import bibtexparser
from bibtexparser.bparser import BibTexParser

ROOT = Path(__file__).parent
DATA = ROOT / "data"
TEMPLATES = ROOT / "templates"


# ---------------------------------------------------------------------------
# Author formatting:  "Last, First Middle"  ->  "Last, F.M."
# ---------------------------------------------------------------------------

_INITIAL_RE = re.compile(r"^[A-Za-z]")


def _initials(first: str) -> str:
    """'Siu Lun' -> 'S.L.', 'Jean-Francois' -> 'J.-F.', no internal spaces."""
    pieces = []
    for token in first.split():
        if not token:
            continue
        if "-" in token:
            sub = [t[0].upper() + "." for t in token.split("-") if t and _INITIAL_RE.match(t)]
            if sub:
                pieces.append("-".join(sub))
        elif _INITIAL_RE.match(token):
            pieces.append(token[0].upper() + ".")
    return "".join(pieces)


# Drop trailing parenthetical notes that bibtex authors sometimes carry,
# e.g. "Muandet (*denotes co-first), Krikamol" or "Sejdinovic, Dino (* denotes cofirst)".
_PAREN_NOTE_RE = re.compile(r"\s*\([^)]*\)")


def format_author(name: str) -> str:
    name = _PAREN_NOTE_RE.sub("", name).strip()
    if not name:
        return ""
    if "," in name:
        last, first = [p.strip() for p in name.split(",", 1)]
    else:
        parts = name.split()
        last, first = parts[-1], " ".join(parts[:-1])
    init = _initials(first)
    return f"{last}, {init}" if init else last


def join_authors(field: str, bold_re: re.Pattern | None = None) -> str:
    # Strip "(* denotes cofirst)" notes embedded in any author segment.
    cleaned = _PAREN_NOTE_RE.sub("", field)
    parts = [format_author(a) for a in cleaned.split(" and ") if a.strip()]
    joined = ", ".join(parts)
    # Strip ONE trailing period (so the template's sentence period doesn't
    # produce "P..") -- but only on the *whole* string, so intermediate
    # initials keep their periods.
    if joined.endswith("."):
        joined = joined[:-1]
    if bold_re is not None:
        joined = bold_re.sub(r"\\textbf{\g<0>}", joined)
    return joined


def make_bold_pattern(surname: str, initials: str) -> re.Pattern:
    """Build a regex matching e.g. 'Chau, S.L.', 'Chau*, S.L', 'Chau, S.L.'.

    initials="S.L." -> regex piece 'S\\.L\\.?' (final period optional, since
    join_authors strips it on the last author).
    """
    init_letters = [c for c in initials if c.isalpha()]
    if not init_letters:
        return re.compile(r"(?!x)x")  # match nothing
    init_re = r"\.".join(init_letters) + r"\.?"
    return re.compile(rf"{re.escape(surname)}\*?,\s+{init_re}")


# ---------------------------------------------------------------------------
# Publication classification + venue cleanup
# ---------------------------------------------------------------------------

_CONFERENCE_KEYWORDS = [
    "conference",
    "neurips",
    "icml",
    "aaai",
    "aistats",
    "uai",
    "iclr",
    "advances in neural",
    "proceedings",
    "international conference",
    "joint european",
    "pmlr",
    "ecml",
    "kdd",
]


def classify(entry: dict) -> str:
    venue = (entry.get("journal") or entry.get("booktitle") or "").lower()
    etype = entry.get("ENTRYTYPE", "").lower()

    if "arxiv preprint" in venue or "preprint" in venue:
        return "working"
    if any(k in venue for k in _CONFERENCE_KEYWORDS):
        return "conference"
    if etype == "inproceedings":
        return "conference"
    if etype == "article":
        return "journal"
    if etype == "phdthesis":
        return "other"
    return "other"


def clean_venue(entry: dict) -> str:
    venue = (
        entry.get("journal")
        or entry.get("booktitle")
        or entry.get("school")        # phdthesis/mastersthesis
        or entry.get("publisher")
        or ""
    ).strip()
    # "arXiv preprint arXiv:1234.56789" -> "arXiv:1234.56789"
    m = re.match(r"arXiv preprint (arXiv:[\d.v]+)", venue)
    if m:
        return m.group(1)
    return venue


def strip_braces(s: str) -> str:
    # bibtexparser sometimes preserves {Protected} braces in titles.
    return s.replace("{", "").replace("}", "")


def coerce_year(s) -> int | str:
    s = str(s).strip()
    return int(s) if s.isdigit() else s


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def load_publications(bib_path: Path, bold_re: re.Pattern | None = None) -> dict:
    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    with bib_path.open(encoding="utf-8") as f:
        db = bibtexparser.load(f, parser=parser)

    entries = []
    for e in db.entries:
        entries.append({
            "key": e.get("ID", ""),
            "type": e.get("ENTRYTYPE", ""),
            "title": strip_braces(e.get("title", "")).rstrip("."),
            "authors": join_authors(e.get("author", ""), bold_re=bold_re),
            "venue": clean_venue(e),
            "year": coerce_year(e.get("year", "")),
            "pdf": e.get("pdf", "").strip(),
            "code": e.get("code", "").strip(),
            "video": e.get("video", "").strip(),
            "award": e.get("award", "").strip(),
            "category": classify(e),
        })

    def _assign_numbers(items, prefix):
        """Number chronologically (oldest = 1, newest = N), return newest-first
        for display so the highest number sits on top."""
        chrono = sorted(
            items,
            key=lambda e: (
                e["year"] if isinstance(e["year"], int) else 0,
                e["key"],
            ),
        )
        for i, e in enumerate(chrono, start=1):
            e["label"] = f"{prefix}{i}"
        return list(reversed(chrono))

    return {
        "journal":    _assign_numbers([e for e in entries if e["category"] == "journal"], "J"),
        "conference": _assign_numbers([e for e in entries if e["category"] == "conference"], "C"),
        "working":    _assign_numbers([e for e in entries if e["category"] == "working"], "W"),
        "other":      [e for e in entries if e["category"] == "other"],
    }


def load_yaml(name: str):
    path = DATA / f"{name}.yaml"
    if not path.exists():
        return None
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_bibliometrics(b: dict | None, today: str):
    """Pre-render the bibliometrics section into ready-to-emit LaTeX strings.
    Returns None when all three counts are blank, so the partial auto-hides."""
    if not b:
        return None
    citations = (b.get("citations") or "").strip()
    h_index   = (b.get("h_index") or "").strip()
    i10_index = (b.get("i10_index") or "").strip()
    if not (citations or h_index or i10_index):
        return None

    parts = []
    if citations:
        parts.append(f"Total citations: \\textbf{{{citations}}}")
    if h_index:
        parts.append(f"h-index: \\textbf{{{h_index}}}")
    if i10_index:
        parts.append(f"i10-index: \\textbf{{{i10_index}}}")
    sep = " \\quad\\textcolor{accent}{\\textbullet}\\quad "
    metrics_line = sep.join(parts) + "."

    source = (b.get("source") or "Google Scholar").strip()
    url    = (b.get("url") or "").strip()
    as_of  = (b.get("as_of") or "").strip() or today

    source_str = f"\\href{{{url}}}{{{source}}}" if url else source
    caption = f"Source: {source_str}, as of {as_of}."

    return {"metrics_line": metrics_line, "caption": caption}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv=None):
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        # LaTeX-safe delimiters so we don't clash with TeX's own { } and %.
        block_start_string="<%",
        block_end_string="%>",
        variable_start_string="<<",
        variable_end_string=">>",
        comment_start_string="<#",
        comment_end_string="#>",
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )

    meta = load_yaml("meta") or {}
    bold_cfg = meta.get("bold_self") or {}
    bold_re = (
        make_bold_pattern(bold_cfg["surname"], bold_cfg["initials"])
        if bold_cfg.get("surname") and bold_cfg.get("initials")
        else None
    )

    positions = load_yaml("positions") or []
    for p in positions:
        p.setdefault("type", "academic")

    context = {
        "meta": meta,
        "positions": positions,
        "education": load_yaml("education") or [],
        "awards": load_yaml("awards") or [],
        "talks": load_yaml("talks") or {},
        "service": load_yaml("service") or {},
        "funding": load_yaml("funding") or [],
        "teaching": load_yaml("teaching") or [],
        "students": load_yaml("students") or {},
        "examinations": load_yaml("examinations") or [],
        "reviewing": load_yaml("reviewing") or {},
        "references": load_yaml("references") or [],
        "publications": load_publications(ROOT / "publications.bib", bold_re=bold_re),
        "today": date.today().strftime("%B %-d, %Y"),
    }
    context["bibliometrics"] = render_bibliometrics(
        load_yaml("bibliometrics"), context["today"]
    )

    template = env.get_template("cv.tex.j2")
    output = template.render(**context)

    out_path = ROOT / "cv.tex"
    out_path.write_text(output, encoding="utf-8")
    pubs = context["publications"]
    total = sum(len(v) for v in pubs.values())
    print(f"Wrote {out_path.relative_to(ROOT)}")
    print(
        f"  Publications: {total} total "
        f"({len(pubs['journal'])} journal, "
        f"{len(pubs['conference'])} conference, "
        f"{len(pubs['working'])} working, "
        f"{len(pubs['other'])} other)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
