-- 代码块 → Word 样式“代码”
function CodeBlock (el)
  el.attributes['custom-style'] = '代码'
  return el
end

-- 标题 1/2 → Word 样式“标题 1/2”
function Header (el)
  if el.level == 1 then
    el.attributes['custom-style'] = '标题 1'
  elseif el.level == 2 then
    el.attributes['custom-style'] = '标题 2'
  end
  return el
end

-- 引用块 → Word 样式“引用”
function BlockQuote (el)
  return pandoc.Div(el.content, {["custom-style"] = '引用'})
end