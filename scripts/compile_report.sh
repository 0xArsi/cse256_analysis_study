#!/bin/bash
pdflatex --output-directory=$(pwd)/report/ ./report/report.tex
bibtex --output-directory=$(pwd)/report/ ./report/report.aux
pdflatex --output-directory=$(pwd)/report/ ./report/report.tex
pdflatex --output-directory=$(pwd)/report/ ./report/report.tex