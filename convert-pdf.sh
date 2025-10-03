#!/usr/bin/env bash

## 方式一：直接生成 PDF
# pandoc README.md -o output.pdf \
#   --from markdown \
#   --to html5 \
#   --template=custom_template.html \
#   --pdf-engine=wkhtmltopdf

## 方式二：先生成 HTML，再用 weasyprint 转 PDF
pandoc README.md -o output.html \
  --css=custom_style.css \
  --template=custom_template.html 
echo "生成完成：output.html"
weasyprint output.html output.pdf

echo "转换完成：output.pdf"
open output.pdf