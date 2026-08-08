***VIM***

---
Vim是一种轻量文本编辑器

配置 Vim 主要通过修改其配置文件 `.vimrc` 来实现。可以把它想象成 Vim 的“控制面板”，所有个性化的设置、快捷键和插件都在这里定义。

**用户配置文件**：位于 `~/.vimrc`。如果文件不存在，你需要自己创建它[](https://cloud.tencent.com.cn/developer/information/vimrc%E9%85%8D%E7%BD%AE%E8%AF%A6%E8%A7%A3-article)。
**全局配置文件**：位于 `/etc/vimrc`，会影响所有用户[](https://wiki.archlinux.org/title/Vim)。

```
set number          " 行号，方便你定位
syntax on           " 高亮，方便你阅读
set ruler           " 右下角显示位置
set showcmd         " 右下角显示你正在输入的命令（学习阶段非常有用）
set hlsearch        " 搜索高亮
set incsearch       " 边输入边跳
```


配置vim使其能读取系统剪切板
`vim --version | grep clipboard`
```
ubuntuX@DESKTOP-DA4HN7Q:~/editor_test$ vim --version | grep clipboard
-clipboard         +keymap            +printer           +vertsplit
+emacs_tags        +mouse_gpm         -sun_workshop      -xterm_clipboard

-clipboard 表示不支持
```
那就需要安装一个东西来令其支持
`sudo apt install vim-gtk3`
# 记录
复制黏贴
整体处理
跳转
移动
查找
替换