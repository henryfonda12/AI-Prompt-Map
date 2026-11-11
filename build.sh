#!/bin/sh
# Rebuild the map from source/ai-prompt-map.md
set -e
cd "$(dirname "$0")"
python3 -I src/parse.py source/ai-prompt-map.md dist/data.json
python3 -I src/build.py src/template.html dist/data.json dist/artifact.html
# Standalone page: opens with a double-click in any browser
{ printf '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>[hidden]{display:none!important}body{margin:0}</style>'; cat dist/artifact.html; } > index.html
echo "Done: index.html"
