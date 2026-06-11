#!/bin/bash
# Converts /tmp/trip-plan.md to ~/Desktop/trip-plan.pdf using pandoc.
# Falls back to pdflatex if xelatex is unavailable.
set -e

INPUT="/tmp/trip-plan.md"
OUTPUT="$HOME/Desktop/trip-plan.pdf"

if ! command -v pandoc &>/dev/null; then
  echo "pandoc not found" >&2
  exit 1
fi

if pandoc "$INPUT" -o "$OUTPUT" --pdf-engine=xelatex \
    -V geometry:margin=2cm \
    --metadata title="Israel Day Trip Plan" 2>/dev/null; then
  echo "Saved to $OUTPUT"
elif pandoc "$INPUT" -o "$OUTPUT" --pdf-engine=pdflatex \
    -V geometry:margin=2cm \
    --metadata title="Israel Day Trip Plan"; then
  echo "Saved to $OUTPUT"
else
  echo "PDF generation failed" >&2
  exit 1
fi
