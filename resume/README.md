# CV — Siu Lun Chau

A modular, data-driven LaTeX CV. Each section lives in its own file; a small
Python build step renders everything into a single `cv.tex` that compiles to
`cv.pdf`.

## Layout

```
.
├── data/                       <- one YAML file per section (edit these!)
│   ├── meta.yaml               <- name, titles, research interests
│   ├── positions.yaml          <- academic positions
│   ├── education.yaml          <- education
│   ├── awards.yaml             <- awards & recognition
│   ├── talks.yaml              <- invited talks + guest lectures
│   ├── service.yaml            <- workshops, memberships
│   ├── funding.yaml            <- grants
│   ├── teaching.yaml           <- courses
│   └── students.yaml           <- supervision (postdocs / PhD / UG-MSc)
├── publications.bib            <- master bibliography (edit directly)
├── templates/
│   ├── cv.tex.j2               <- master LaTeX template
│   └── partials/               <- one Jinja2 partial per section
├── build.py                    <- YAML + .bib  →  cv.tex
├── Makefile                    <- convenience targets
├── cv.tex                      <- generated; DO NOT edit by hand
└── cv.pdf                      <- final output
```

## Usage

```bash
make            # full rebuild: render + latex
make render     # just regenerate cv.tex (no compile)
make pdf        # just compile cv.tex → cv.pdf
make watch      # continuous rebuild (latexmk -pvc)
make clean      # remove aux files (keep cv.pdf)
make distclean  # nuke everything generated
```

Requirements: `python3` with `pyyaml`, `jinja2`, and `bibtexparser` installed;
a working TeX Live with `pdflatex` and `latexmk`. To install the Python
dependencies one-off:

```bash
pip3 install pyyaml jinja2 bibtexparser
```

## How to edit

### Adding a publication

Open `publications.bib` and add a new BibTeX entry. The build script
classifies entries automatically:

| Where it lands             | Rule                                       |
|----------------------------|--------------------------------------------|
| Working Papers / Under Review | `journal` contains "arXiv preprint"  |
| Conference Papers          | `@inproceedings`, or venue mentions ICML / NeurIPS / AAAI / AISTATS / UAI / ICLR / "Conference" / "Proceedings" / PMLR / ECML / KDD |
| Journal Papers             | other `@article` entries                   |
| Theses                     | `@phdthesis`                               |

Optional non-standard fields that become clickable badges:

```bibtex
pdf   = {https://...}    % becomes [pdf]
code  = {https://...}    % becomes [code]
video = {https://...}    % becomes [video]
award = {Spotlight}      % shown in italics as "(Spotlight)"
```

### Adding a talk

Edit `data/talks.yaml`. Multiple years at the same venue go in the `years`
list:

```yaml
- years: [2026, 2024]
  venue: "LMU Munich"
```

### Adding a student / position / award / etc.

Open the corresponding YAML file and add a new entry under the right list.
Each section's schema is documented as comments at the top of its YAML file.

### Adding a photo

Drop your photo (`.jpg`, `.png`, or `.pdf`) anywhere inside the project folder,
then set in `data/meta.yaml`:

```yaml
photo: "photo.jpg"          # or "assets/headshot.png", etc.
photo_width: "3cm"          # how wide it should appear on the page
```

The header switches to a two-column layout (name and titles on the left,
photo on the right). Leave `photo: ""` to revert to the centred, no-photo
header.

For best results: crop the image to a square or portrait aspect ratio before
saving — `\includegraphics` will preserve the source aspect ratio.

### Special characters in YAML

The YAML files are read **literally as LaTeX**. That means:

- `&` → `\\&`  (in YAML; renders as `\&` in LaTeX)
- `%` → `\\%`
- `_` → `\\_`
- `#` → `\\#`
- en-dash → `--`
- em-dash → `---`
- accented characters either as `\\'e` or directly (UTF-8 is fine).

If a section is missing or empty the corresponding heading is skipped
automatically.

## How it works (the 60-second tour)

1. `build.py` reads every `data/*.yaml` into a Python dict.
2. It parses `publications.bib` with `bibtexparser`, normalises author names
   to `"Lastname, F.M."` style, classifies entries, and sorts by year.
3. Jinja2 (configured with LaTeX-safe delimiters `<%`, `<<`, `>>`, `%>`)
   renders `templates/cv.tex.j2`, which `{% include %}`s the partials in
   `templates/partials/`.
4. The result is one `cv.tex`. `latexmk -pdf cv.tex` produces `cv.pdf`.

To change the **look** (colours, fonts, spacing, section order), edit
`templates/cv.tex.j2`. To change the **content**, edit the YAML files or the
bib.
