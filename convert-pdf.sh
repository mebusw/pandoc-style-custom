#!/usr/bin/env bash
pandoc README.md -o output.pdf \
  --template=custom_template.html 

echo "转换完成：output.pdf"
open output.pdf