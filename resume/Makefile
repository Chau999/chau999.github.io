# CV build pipeline.
#   make            -- render YAML+bib -> cv.tex, then compile cv.pdf
#   make render     -- just YAML/bib -> cv.tex (no LaTeX run)
#   make pdf        -- just cv.tex -> cv.pdf
#   make watch      -- continuous rebuild on file changes (needs latexmk -pvc)
#   make clean      -- remove LaTeX aux files (keep cv.pdf)
#   make distclean  -- remove everything generated

LATEX        := pdflatex
LATEXMK      := latexmk
LATEXMKOPTS  := -pdf -interaction=nonstopmode -halt-on-error -file-line-error
PY           := python3

DATA_FILES   := $(wildcard data/*.yaml)
TPL_FILES    := $(wildcard templates/*.j2) $(wildcard templates/partials/*.j2)

.PHONY: all render pdf watch clean distclean

all: cv.pdf

cv.tex: build.py publications.bib $(DATA_FILES) $(TPL_FILES)
	$(PY) build.py

render: cv.tex

pdf: cv.pdf

cv.pdf: cv.tex
	$(LATEXMK) $(LATEXMKOPTS) cv.tex

watch: cv.tex
	$(LATEXMK) $(LATEXMKOPTS) -pvc cv.tex

clean:
	$(LATEXMK) -c cv.tex 2>/dev/null || true
	rm -f cv.aux cv.log cv.out cv.toc cv.fls cv.fdb_latexmk

distclean: clean
	rm -f cv.tex cv.pdf
