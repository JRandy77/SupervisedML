#!/usr/bin/env bash

# Input and output directories
MD_DIR="Slides/markdown"
PDF_DIR="Slides/PDFs"

# Theme settings
THEME_PATH="./themes/micm_theme.css"
THEME_NAME="micm_theme"

# Ensure input exists
if [ ! -d "$MD_DIR" ]; then
  echo "Error: Markdown directory '$MD_DIR' does not exist."
  exit 1
fi

# Ensure output directory exists
mkdir -p "$PDF_DIR"

# Process each markdown file
for FILE in "$MD_DIR"/*.md; do
  BASENAME="$(basename "$FILE" .md)"
  OUTPUT="$PDF_DIR/$BASENAME.pdf"

  echo "Generating PDF for: $BASENAME.md"

  npx marp "$FILE" \
    --theme-set "$THEME_PATH" \
    --theme "$THEME_NAME" \
    --pdf \
    --allow-local-files \
    -o "$OUTPUT"
done

echo "Done! PDFs saved in '$PDF_DIR/'"

