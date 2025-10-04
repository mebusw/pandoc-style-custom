import os
import re
import hashlib
import mermaid as md
from typing import Optional

# --- 配置 ---
# 要处理的 Markdown 文件路径
MARKDOWN_FILE = 'README.md' 
# 存放生成图片的目录
IMAGE_DIR = 'output'
# 匹配 Mermaid 代码块的正则表达式：匹配被 ```mermaid ... ``` 包裹的内容
MERMAID_PATTERN = re.compile(r"```(?:mermaid|mer|mmd)\s*\n(.*?)\n```", re.DOTALL | re.IGNORECASE)


def render_mermaid_to_png(mermaid_code: str, output_path: str) -> Optional[str]:
    """
    使用 mermaid-py 将 Mermaid 语法渲染为 PNG 文件。
    
    Args:
        mermaid_code: Mermaid 语法字符串。
        output_path: 完整的输出文件路径（包括文件名和扩展名）。
        
    Returns:
        成功时返回图片链接路径，失败时返回 None。
    """
    try:
        render = md.Mermaid(mermaid_code)
        
        # 使用 to_png() 方法获取字节数据
        png_bytes = render.to_png(output_path)
            
        return output_path
    except Exception as e:
        print(f"❌ 渲染失败 (文件: {output_path}): {e}")
        return None


def process_markdown_file(md_filepath: str, img_output_dir: str):
    """
    扫描 Markdown 文件，转换其中的 Mermaid 代码块为图片并替换链接。
    """
    if not os.path.exists(md_filepath):
        print(f"❌ 错误：找不到文件 '{md_filepath}'。")
        return

    # 确保图片输出目录存在
    os.makedirs(img_output_dir, exist_ok=True)
    
    print(f"--- 正在处理文件: {md_filepath} ---")
    
    # 1. 读取文件内容
    with open(md_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 用于保存所有代码块和对应链接的映射
    replacements = {}
    
    # 使用 re.findall 来获取所有匹配到的 Mermaid 语法块
    mermaid_blocks = MERMAID_PATTERN.findall(content)

    if not mermaid_blocks:
        print("ℹ️ 未找到任何 Mermaid 代码块。")
        return

    print(f"🔍 找到 {len(mermaid_blocks)} 个 Mermaid 代码块。")

    # 2. 遍历并渲染每个代码块
    for i, code in enumerate(mermaid_blocks):
        # 使用代码内容的 SHA256 哈希值作为文件名，确保内容不变时文件名不变（幂等性）
        code_hash = hashlib.sha256(code.encode('utf-8')).hexdigest()[:12]
        
        # 构造图片文件名和路径
        # 例如: images/diagram-a0b1c2d3e4f5.png
        img_filename = f"diagram-{code_hash}.png"
        img_full_path = os.path.join(img_output_dir, img_filename)
        
        # 相对路径，用于 Markdown 链接
        img_relative_path = os.path.join("", img_filename)
        
        # 检查图片是否已经存在，如果存在则跳过渲染（节省 API 调用次数）
        if os.path.exists(img_full_path):
            print(f"跳过渲染 {i+1}/{len(mermaid_blocks)}: 图片已存在 ({img_filename})")
        else:
            print(f"正在渲染 {i+1}/{len(mermaid_blocks)}... ({img_filename})")
            
            # 渲染并保存
            render_success_path = render_mermaid_to_png(code, img_full_path)
            if not render_success_path:
                continue # 渲染失败，跳过替换

        # 构造替换用的 Markdown 链接
        # 注意：这里我们使用原始代码块作为字典的键，以便后续的 re.sub 替换
        original_block = f"```mermaid\n{code}\n```"
        markdown_link = f"![]({img_relative_path})"
        
        # 将原始代码块和替换链接存储起来
        replacements[original_block] = markdown_link


    # 3. 替换内容并写入新文件
    
    # 构造一个新的文件名，例如 'input_with_images.md'
    base, ext = os.path.splitext(md_filepath)
    new_filepath =  os.path.join(img_output_dir, f"{base}_with_images{ext}") 
    
    new_content = content
    # 从替换字典中替换内容
    # 注意：我们必须从最长的匹配开始替换，以防万一有嵌套（虽然mermaid代码块不应嵌套）
    # 但简单起见，我们直接对整个文档进行替换。
    for original_block, markdown_link in replacements.items():
        # 这里使用 re.escape 来确保原始代码中的特殊字符不会被当作正则表达式的一部分
        # 只替换第一次出现的匹配项，以防重复
        new_content = re.sub(re.escape(original_block), markdown_link, new_content, count=1)


    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"\n✅ 处理完成！")
    print(f"原始文件: {md_filepath}")
    print(f"新文件（已替换图片链接）已保存到: {new_filepath}")
    print(f"所有生成的图片位于: {img_output_dir}/")


if __name__ == "__main__":
    # --- 运行脚本 ---
    # 假设你的原始文件名为 'README.md'
    # 请根据实际情况修改 MARKDOWN_FILE 的值
    process_markdown_file(MARKDOWN_FILE, IMAGE_DIR)