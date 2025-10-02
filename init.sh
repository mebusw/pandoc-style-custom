#!/usr/bin/env bash
set -e
echo "正在生成 custom-reference.docx …"
pandoc -o custom-reference.docx --print-default-data-file reference.docx
cat << EOF
请在 Word 中打开 custom-reference.docx 并修改样式（必须改“样式”本身）：
  标题 1   黑体 小二 加粗
  标题 2   黑体 三号 加粗
  正文     宋体 小四 1.5 倍行距
  代码     Consolas 10pt 淡灰背景
  引用     楷体 小四 斜体 左缩进 2 字
EOF
open custom-reference.docx || open -a "wpsoffice.app" custom-reference.docx || open -a "Microsoft Word" custom-reference.docx || xdg-open custom-reference.docx