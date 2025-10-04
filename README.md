---
title: 传承测评报告
author: 章动咨询
date: 2025-09-30
subtitle: 宗馥莉
---
# 一级标题
[TOC]

这是正文段落，演示**样式继承**。

## 二级标题

```python
print("Hello, Pandoc!")
```

> 这是一个引用块，将使用“引用”样式。

![](./sample-client-drawing.png)

### ✅ 使用步骤（复制以上文件到同一目录）
1. 双击 `init.bat` / 运行 `./init.sh`  (注意添加运行权限)
   → 自动生成 `custom-reference.docx` 并提示你改样式。
2. 在 Word 里把样式改好并保存。
3. 把 `README.md` 换成你自己的内容。
4. 双击 `convert.bat` / 运行 `./convert.sh`  
   → 得到 `output.docx`，样式完全按你定义的来。


| Name | Addr | Phone |
| ---- | ---- | ----- |
| 张三 | 天津 | 123   |
| 李四 | 北京 | 456   |
| 王五 | 上海 | 789   |



### 列表
- 上海
  - 闵行
  - 青浦
  - 静安
- 天津
- 北京

## 图表
```mermaid
graph TD
    A[开始] --> B{判断};
    B -- 是 --> C[执行操作 1];
    B -- 否 --> D[执行操作 2];
    C --> E[结束];
    D --> E;
```

```mermaid
flowchart TD
 subgraph s1["Untitled subgraph"]
        n3["Untitled Node"]
  end
    A["引言: 改写题目, 介绍图表和表格信息"] --> B("总体概述: 全球水用趋势和两国用水差异")
    B --> C("主体段落1: 柱状图细节描述") & D("主体段落2: 表格细节描述")
    C --> C1("农业用水的主导地位和趋势") & C2("工业和家庭用水的增长") & C3("引用关键数据支持")
    D --> D1("巴西和刚果的水用对比") & D2("各部门用水比例及人均用水量") & D3("引用关键数据进行比较")
    n1["Sample Label"] --> n2["Untitled Node"]
    n1@{ icon: "mc:default", pos: "b"}
```


```mermaid
sequenceDiagram
    participant User
    participant Server
    User->>Server: 请求数据
    Server-->>User: 返回数据
```
