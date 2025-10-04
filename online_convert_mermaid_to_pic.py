import mermaid as md
from mermaid.graph import Graph

# 1. 定义 Mermaid 语法
mermaid_code = """
graph TD
    A[开始] --> B{判断};
    B -- 是 --> C[执行操作 1];
    B -- 否 --> D[执行操作 2];
    C --> E[结束];
    D --> E;
"""

# 2. 创建 Mermaid 对象
# Graph类用于构建，但这里我们直接使用 Mermaid 类来处理字符串
# draw_method 默认为 'api'，即使用 mermaid.ink
render = md.Mermaid(mermaid_code)

# 3. 渲染并保存为文件
output_file = "output.png"
print(f"正在将 Mermaid 渲染为 {output_file}...")
try:
    png_bytes = render.to_png(output_file)
    # 如果想保存为 SVG，可以指定 to_svg(output_file)
    
    print(f"✅ 成功保存图片到：{output_file}")
except Exception as e:
    print(f"❌ 渲染失败，可能是网络问题或 mermaid.ink 服务不可用: {e}")