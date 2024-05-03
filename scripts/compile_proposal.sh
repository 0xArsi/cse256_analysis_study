#!/bin/bash
pdflatex --output-directory=$(pwd)/proposal/ ./proposal/proposal.tex
bibtex --output-directory=$(pwd)/proposal/ ./proposal/proposal.aux
pdflatex --output-directory=$(pwd)/proposal/ ./proposal/proposal.tex
pdflatex --output-directory=$(pwd)/proposal/ ./proposal/proposal.tex