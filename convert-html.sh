#!/usr/bin/env bash

pandoc README.md -o output.html \
  --template=custom_template.html 

echo "转换完成：output.html"
open output.html