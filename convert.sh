#!/usr/bin/env bash
pandoc README.md -o output.docx \
  --reference-doc=custom-reference.docx \
  --lua-filter=style-filter.lua
echo "转换完成：output.docx"
open output.docx || open -a "wpsoffice.app" output.docx || open -a "Microsoft Word" output.docx || xdg-open output.docx