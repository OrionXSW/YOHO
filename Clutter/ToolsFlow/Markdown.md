# Markdown 语法教学文档

> Markdown 是一种轻量级标记语言，它允许人们使用易读易写的纯文本格式编写文档，然后转换成有效的 HTML。

---
待补充:图片管理

## 1. 标题

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

### 效果：

# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

---

## 2. 段落与换行

段落之间用**一个空行**分隔。

这是第一段文字。  
行尾加两个空格 + 回车 → 强制换行（或使用 `<br>` 标签）。

这是第二段文字。

---

## 3. 字体样式

```markdown
*斜体*         或 _斜体_
**粗体**       或 __粗体__
***粗斜体***   或 ___粗斜体___
~~删除线~~
==高亮==（某些解析器支持）
<u>下划线</u>（使用 HTML 标签）
```

### 效果：

- *斜体*
- **粗体**
- ***粗斜体***
- ~~删除线~~
- <u>下划线</u>

---

## 4. 列表

### 无序列表

```markdown
- 项目一
- 项目二
  - 子项目 2.1
  - 子项目 2.2
- 项目三
```

### 效果：

- 项目一
- 项目二
  - 子项目 2.1
  - 子项目 2.2
- 项目三

---

### 有序列表

```markdown
1. 第一步
2. 第二步
3. 第三步
   1. 子步骤 3.1
   2. 子步骤 3.2
```

### 效果：

1. 第一步
2. 第二步
3. 第三步
   1. 子步骤 3.1
   2. 子步骤 3.2

---

### 任务列表

```markdown
- [x] 已完成任务
- [ ] 未完成任务
- [ ] 待办事项
```

### 效果：

- [x] 已完成任务
- [ ] 未完成任务
- [ ] 待办事项

---

## 5. 链接

```markdown
[显示文字](https://www.example.com "鼠标悬停提示")

[带 ID 的引用式链接][link-id]

[link-id]: https://www.example.com "可选标题"
```

### 效果：

[GitHub](https://github.com "全球最大的代码托管平台")

[引用式链接][example-link]

[example-link]: https://www.example.com

---

### 自动链接

```markdown
<https://www.example.com>
<email@example.com>
```

<https://www.example.com>

---

## 6. 图片

```markdown
![替代文字](图片URL "鼠标悬停提示")

![本地图片](./images/example.png)
```

![占位图片](https://via.placeholder.com/150 "示例图片")

---

## 7. 代码

### 行内代码

```markdown
使用 `printf("Hello, World!");` 打印输出。
```

效果：使用 `printf("Hello, World!");` 打印输出。

---

### 代码块（使用三个反引号）

````markdown
```python
def hello():
    print("Hello, Markdown!")
```
````

### 效果：

```python
def hello():
    print("Hello, Markdown!")
```

````markdown
```javascript
const greeting = "Hello";
console.log(`${greeting}, Markdown!`);
```
````

### 效果：

```javascript
const greeting = "Hello";
console.log(`${greeting}, Markdown!`);
```

---

### 缩进式代码块（4 个空格或 1 个 Tab）

    这是一段缩进代码。
    每行前面加 4 个空格或 1 个 Tab。
    不需要指定语言。

---

## 8. 引用

```markdown
> 这是一段引用。
>
> > 这是嵌套引用。
>
> 引用可以包含 **Markdown** 语法。
```

### 效果：

> 这是一段引用。
>
> > 这是嵌套引用。
>
> 引用可以包含 **Markdown** 语法。

---

## 9. 分割线

三种写法（效果相同）：

```markdown
---
***
___
```

---

***

___

---

## 10. 表格

```markdown
| 左对齐  |  居中   | 右对齐 |
| :------ | :----: | -----: |
| 单元格  | 单元格 |  单元格 |
| 单元格  | 单元格 |  单元格 |
```

### 效果：

| 左对齐  |  居中   | 右对齐 |
| :------ | :----: | -----: |
| 单元格  | 单元格 |  单元格 |
| 单元格  | 单元格 |  单元格 |

---

## 11. 脚注

```markdown
这里有一个脚注[^1]。

[^1]: 这是脚注的解释内容。
```

### 效果：

这里有一个脚注[^1]。

[^1]: 这是脚注的解释内容。

---

## 12. 转义字符

在 Markdown 中，如果需要显示原本有特殊含义的字符，可在前面加反斜杠 `\`。

```markdown
\* 这不是斜体 \*
\# 这不是标题
\[这不是链接\]
```

### 效果：

\* 这不是斜体 \*

\# 这不是标题

\[这不是链接\]

---

## 13. 表情符号

```markdown
:smile: :heart: :+1: :rocket: :fire:
```

### 效果：​

😄 ❤️ 👍 🚀 🔥

---

## 14. HTML 混用

Markdown 支持直接嵌入 HTML 标签。

```html
<p style="color: red;">红色文字段落</p>
<details>
  <summary>点击展开</summary>
  这是隐藏的内容。
</details>
```

### 效果：

<p style="color: red;">红色文字段落</p>

<details>
  <summary>点击展开</summary>
  这是隐藏的内容。
</details>

---

## 15. 数学公式（KaTeX / LaTeX）

> 需要 Markdown 解析器支持（如 GitHub、Typora 等）。

```latex
行内公式：$E = mc^2$

块级公式：
$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$
```

### 效果：

行内公式：$E = mc^2$

块级公式：

$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$

---

## 综合示例

```markdown
# 项目 README

> 这是一个**示例项目**，用于演示 Markdown 的完整语法。

## 功能特性

- [x] 支持标题、段落、列表
- [x] 支持代码块与高亮
- [ ] 支持流程图（需扩展）

## 快速开始

```bash
git clone https://github.com/user/project.git
cd project
npm install
```

## API 文档

| 方法   | 路径       | 说明     |
| ------ | ---------- | -------- |
| GET    | /api/users | 获取用户 |
| POST   | /api/users | 创建用户 |
| DELETE | /api/users | 删除用户 |

## 参考资料

1. [Markdown 官方文档](https://daringfireball.net/projects/markdown/)
2. [GitHub Flavored Markdown](https://github.github.com/gfm/)
```

---

> **提示：** 大部分 Markdown 编辑器（如 VS Code、Typora、Obsidian）都支持实时预览。推荐边写边看效果，上手更快。

---

*Happy Markdown Writing!* 🚀