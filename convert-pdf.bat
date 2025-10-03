@echo off

:: 切换到脚本所在的目录（可选，但推荐）
:: cd /d "%~dp0"

echo 正在使用 Pandoc 生成 output.html...

:: 先生成 HTML (注意：Windows 中行末的反斜杠 \ 不适用，必须用 ^ 来进行多行命令转义)
pandoc README.md -o output.html ^
  --css=custom_style.css ^
  --template=custom_template.html

if errorlevel 1 (
    echo Pandoc 生成 HTML 失败!
    goto :end
)

echo.
echo 生成完成：output.html

echo 正在使用 WeasyPrint 转换 PDF...
weasyprint output.html output.pdf

if errorlevel 1 (
    echo WeasyPrint 转换 PDF 失败!
    goto :end
)

echo.
echo 转换完成：output.pdf

:: 在 Windows 上使用 'start' 命令替代 'open' 来打开文件
start output.pdf

:end
echo.
pause