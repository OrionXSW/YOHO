***Mark Git down Version 2***

-------------------------
# 前置
Git作为一种版本管理工具，能很好地满足管理项目文件的需求

# 仓库初始化
#空白文件夹 #原本有仓库
[命令]: git init
初始化仓库后,git才能发挥作用，这种方法git会以默认分支名的方法给主分支命名，有些是master，有些是main，看git版本
[命令]: git init -b "默认分支名"
以上命令可以自己定义默认分支名，你可以起main,master或者什么其他的

# 账户
账户关系到你要将文件/项目推送的平台
比如添加了github账号或gitee账号,意味着你可以往相应平台的仓库推送文件/项目
经实验，如果不配置用户名和邮箱，Git 会拒绝执行 git commit（会报错提示配置）
[命令]: git config --global user.name "你的名字写这里"
[命令]: git config --global user.email "你的邮箱写这里"
注:这都是应用全局的账户，如下是在单独项目中配置不同的账户
[命令]: git config user.name "项目专用用户名"
[命令]: git config user.email "项目专用邮箱"

查看当前账户情况
(git bash 终端窗口下 3个命令都能查看)
[命令]: git config --global --list | grep user
(vscode内部/windows终端 仅能用下面的命令查看)
[命令]: git config user.name      # 查看用户名
[命令]: git config user.email      # 查看邮箱


# 链接位于托管平台的远程仓库
前提:得有一个托管平台(github,gitee或者其他)，还要有相应的远程仓库
远程链接可通过https或者ssh来实现，http简单很多，但有时可能出现网络问题，需要魔法才好用(推荐一个比较安全的:FastGithub)
ssh配置起来比较麻烦，需要密钥什么的，但不用担心网络问题,并且更安全
https和ssh的文件传输速度差不多
## http实现
[命令]: git remote add <远程仓库别名> <仓库地址.git>
补充: 常见的远程仓库别名有origin(默认的，常用于github仓库的别名)，gitee等等，别名都是自定义的
例: git remote add origin 仓库.git 或 git remote add gitee 仓库.git
**这个仓库地址在托管平台对应仓库中可以看到**
## ssh实现
将本地 Git 仓库通过 SSH 连接到 GitHub，核心是生成 SSH 密钥对 → 上传公钥到 GitHub → 配置本地仓库远程地址 → 测试连接。
### 一、检查/生成SSH密钥(本地)
1.检查是否已有密钥
```
ls ~/.ssh
# 看是否有 id_ed25519 / id_ed25519.pub 或 id_rsa / id_rsa.pub
```
2.生成新密钥(推荐ed25519)
ed25519，是目前生成SSH密钥时最推荐的非对称加密算法
```
# 替换为你 GitHub 注册邮箱
ssh-keygen -t ed25519 -C "your-email@example.com"
```
提示保存路径：直接回车（默认 ~/.ssh/id_ed25519）
提示密码（passphrase）：直接回车两次（免密）
3.复制公钥内容
```
# Linux/macOS
cat ~/.ssh/id_ed25519.pub

# Windows (Git Bash)
cat ~/.ssh/id_ed25519.pub
# 或手动打开文件：C:\Users\你的用户名\.ssh\id_ed25519.pub
```
复制整行内容（以 ssh-ed25519 开头）。
### 二、把公钥添加到GitHub
1.登录 GitHub → 右上角头像 → Settings
2.左侧：SSH and GPG keys → New SSH key
3.填写：
Title: 随便写（如 My Laptop）
Key type: Authentication Key
Key: 粘贴刚才复制的公钥
点 Add SSH key
补充:这添加的是账户公钥，添加后可通过SSH方式链接该账号下任意仓库
### 三、测试SSH连接
`ssh -T git@github.com`
首次会提示:Are you sure you want to continue connecting (yes/no)? → 输入 yes 回车
成功提示:Hi 你的用户名! You've successfully authenticated, but GitHub does not provide shell access.
### 链接
[命令]: git remote add <远程仓库别名> <仓库地址.git>
补充: 常见的远程仓库别名有origin(默认的，常用于github仓库的别名)，gitee等等，别名都是自定义的
例: git remote add origin git@github.com:xxx/xxx.git
### 清除痕迹
如果想删除与账号管理的密钥，不想保留痕迹，在用户目录下的.ssh文件夹里把对应的文件全部删掉，然后在托管平台的公钥管理的地方把对应的删掉即可

### SSH补充

1. SSH的实现方式使得同一个仓库在不同电脑的链接情况不同，比如一台电脑用SSH链接远程仓库，git remote -v能查询到远程仓库链接，而在另一个电脑里是没有这个链接的，除非用SSH链接一次。
2. Git用SSH协议，但SSH协议本身支持密码、密钥两种登录方式
当你用ssh的方式克隆代码时要是发现需要用密码登录，不用惊讶，这也是SSH的一种登录方式
**注意:第一次用SSH访问服务器时会有安全认证，跟着流程走就行**

## 查看当前已配置的远程仓库
[命令]: git remote -v
注:如果没有任何已配置的远程仓库，那什么都不会出现
## 删除错误链接的远程仓库
如果远程仓库添加错了，该命令可断掉和对应远程仓库的链接
[命令]: git remote remove <仓库别名>
例:git remote remove origin


# 常规使用
## 将工作区的文件添加到暂存区
[命令]:git add .
注意:这个是将工作区全部的文件都添加到暂存区，如果想要添加单独的文件，直接git add xxx.xxx即可
提醒一下，在初始化仓库后，如果之前没有任何提交，那么是不能查看分支状态的，必须先提交文件 git add . 将文件存入暂存区
## 将暂存区的文件/项目提交到本地仓库，后面的字符串作为提交的日志
[命令]:git commit -m "commit message"
**经实验，你要在添加完账户后才能提交到本地仓库**
Commit信息内容规范
[命令]: git commit -m "<类型>: <一句话说明白做了什么>"
fix: 修复xxx问题
feat: 实现xxx功能
save: 临时存档，方便回退
chore: 调整配置(适用于改了些无关紧要的东西)
update: 更新xxx
例:git commit -m "save: 临时存档，方便回退"

当你git commit的信息打错字/内容错误时，若未推送到远程
可运行
[命令]:git commit --amend -m "正确的提交日志内容"
## 推送到远程仓库
[命令]:git push -u origin main (或 master，视具体情况而定)
注:main/master仅仅用于举例，可用其他的分支
命令中-u表示将当前仓库当前分支作为默认上游分支，在运行该命令后，如果推送到远程仓库和对应分支的对象都不变，那么可直接用git push，将暂存区的文件推到远程仓库

如果想一个仓库同时推github和gitee,这时候可以把gitee的地址添加到origin中
[命令]:git remote set-url --add origin gitee地址
添加好后，执行 git push 时，会自动把代码推送到 origin 绑定的所有 push 地址(GitHub + Gitee 一起推)
注:当你的托管账号改了名(@的那个，不是你的用户名),链接上的仓库都需要重新设置地址
[命令]:git remote set-url <远程仓库别名> <远程仓库地址>
[命令]:git push origin main   # 推送到 GitHub和Gitee origin后面的分支名得看你想推送到哪个分支

如果不想这样，可以分别推送给不同仓库
[命令]:git push origin main   # 推送到 GitHub
[命令]:git push gitee main    # 推送到 Gitee
前提是
如果你想把已经添加的网址剔除
[命令]:git remote set-url --delete origin gitee地址


# 分支
## branch类
[命令]:git branch 新分支名
仅创建分支不切换
example: git branch feature 	// 创建了一个名为feature的分支

**查看**
[命令]:git branch 或 git branch -a
查看当前所有分支
[命令]:git branch -v
查看当前所有分支的情况(分支名，分支代码，最新提交的信息)
[命令]:git branch -vv
查看当前所处分支的上游分支
**分支管理**
[命令]:git branch -m 新名字
想把当前所处分支的名字改掉
[命令]:git branch -m 旧名字 新名字
改其他分支的名字（不在那个分支上）
[命令]:git branch -d <分支名>
删除分支（安全删除）
[命令]:git branch -D <分支名>
删除分支（强制删除分支）

**改分支名补充**
如果你已经链接有远程仓库，那么只改本地不行，GitHub/Gitee 上的分支名还是旧的，必须同步改远程
注:origin 和 gitee 本质上都是本地 Git 仓库给「远程仓库地址」起的别名
**origin**:Git 里约定俗成的「默认远程仓库别名」，通常指向你第一次绑定的平台（比如 GitHub）。
**gitee**:你自己给 Gitee 远程仓库起的别名（也可以叫别的，比如 gitee、码云、my-gitee）。
step1:先删远程旧分支
[命令]:git push origin --delete 旧名字
这里gitee可能不给删，原因是为了防止崩溃默认分支是不能被删掉的，这里需要去gitee上把默认分支改别的
进入gitee仓库-管理，找到默认分支（选项是保护分支设置），将默认分支改成其他，然后重新试试
step2:把新名字的分支推上去
[命令]:git push -u origin  新名字
step3:建立本地新分支与远程的关联，设置当前分支的上游分支


## checkout类
[命令]:git checkout -b <分支名>
创建并切换到新分支（常用新建分支指令）
[命令]:git checkout <分支名>
切换分支
## switch类
[命令]:git switch -c  <分支名>
Git 2.23版本以上支持的，创建并切换到新分支
[命令]:git switch <分支名>
切换分支

## 分支补充信息
1. Git的工作区是公用的,暂存区，本地仓库，分支，都是独立的
**唯独工作区是所有分支共享的**
这特性就意味着只要两个分支内容都是一致的，那么在工作区的修改能随分支切换去到目标分支，**除非你修改过的那个文件，在两个分支里内容不一致，那么就会报错，不让你切过去**
2. 上游分支upstream
每条本地分支，都可以独立设置自己的上游
本地分支 dev → 可以绑 origin/dev
本地分支 test → 可以绑 origin/test
本地分支 abc → 甚至可以绑 origin/xyz
你切到哪个分支
git push → 只推到这个分支自己的上游
git pull → 只拉这个分支自己的上游
git status 显示的领先 / 落后 → 也是跟自己的上游比
切换分支 = 切换一套独立的 “本地 ↔ 远程” 对应关系。


# 远程协作
**大致流程**
涉及命令: git pull | git add. | git commit -m "xxx" | git push
场景1: 对于同一个文件夹,想在两台电脑上协作编辑
在托管平台创建一个仓库,用一台电脑将文件夹推送其中,另一台电脑需要复制仓库的地址,新建空的文件夹,打开git bash 克隆一下仓库地址([命令]:git clone xxx.git)
每次编辑前先执行 git pull 拉取云端最新代码，编辑完成后再通过 git add .、git commit 和 git push 推送到云端，养成这个习惯能有效减少冲突。git pull 会对比本地与云端的版本新旧:当云端版本比本地新时，Git 会自动拉取并合并更新；当本地与云端版本一致时，会提示已是最新版本；当本地版本比云端更新时，同样不会出现冲突。真正会导致冲突的情况只有一种，就是你和另一台设备同时修改了同一个文件的同一行内容（同一版本下），Git 无法自动判断保留哪一份修改，才需要手动解决。
**details**:你先 pull 了，拿到最新，你开始改文件 A 的第 10 行，同时，别人也改了文件 A 的第 10 行，并且先 push 上去了，你改完后push → 冲突
**你们是在同一个 “最新版本” 基础上，改了同一行。这种情况，你编辑前 pull 了也没用，照样冲突**,这种就比谁最先推送了
## 从远程下载代码
**注:两种方式都会把所有文件，所有分支，所有提交历史，所有代码完整下载到本地**
1. git pull
下载+自动合并，会改本地代码，可能会导致冲突
适合确认无冲突，想快速同步
2. git fetch
仅下载远程最新代码，不会改动本地代码，也不会导致冲突
适合先看远程改了啥，团队协作
安全方式的同步
```
git fetch       # 下载远程更新
git diff main origin/main  # 看看远程改了什么
git merge origin/main    # 手动合并（这时候才可能出冲突）
```


# 日志
重点关注:提交信息、谁、何时、改了啥、为什么改
[命令]: git log
这个命令会进入日志界面，内容有你之前提交的记录以及时间什么的
当你使用 git log时，会自动进入分页器模式（通常是 less）。以下是基本操作:
[向下移动一行]: j 或下方向键
[向上移动一行]: k 或上方向键
[向上翻一页]:  空格键
[向下翻一页]: b
[搜索]: /
向前搜索关键词
n  - 查找下一个匹配 	N       - 查找上一个匹配
g  - 跳转到第一行	    G       - 跳转到最后一行
数字+g    - 跳转到指定行（如 10g）
[退出]:q
[强制退出]:Ctrl + c
[显示当前行位置]: =
[显示帮助]: h

## 快速查看
[命令]:git log --oneline
查看日志概览
[命令]:git log -n
只查看最后n个修改 
[命令]:git log -p README.md
查看文件修改

# 状态查看
[命令]:git status
功能:查看工作区、暂存区状态，显示哪些文件被修改/新增/删除

[命令]:git status -s
功能:简洁模式显示状态

# 版本回退/修改撤回
注意:要使用版本回退，你得有过提交记录，否则不能使用版本回退
需要提醒的是版本回退指在提交的版本之间进行调整，涉及HEAD指针的移动
而在提交完后进行修改，发现不想要了，可直接退回修改，这两个虽然都实现了某种程度的撤回，但本质上是不一样的。

下面是git使用简单示意图
【工作区】--->git add . ---->[暂存区]---git commit -m "xxx"---->[本地仓库] -> git push [远程仓库]
只有提交到本地仓库的才能进行版本回退

## 范围:工作区-暂存区-本地仓库
### 改动仅在「工作区」（未 add、未 commit）
| 操作意图 | 命令 | 说明 |
| :--- | :--- | :--- |
| 丢弃单个文件的修改 | `git restore <file>` <br> 旧写法：`git checkout -- <file>` | 文件恢复到最近一次 commit 或暂存区状态 |
| 丢弃工作区所有修改 | `git restore .` <br> 旧写法：`git checkout .` | 工作区恢复干净，**不删除**新建的未跟踪文件 |
| 删除未跟踪的文件/目录 | `git clean -fd` | `-f` 强制，`-d` 目录。**⚠️ 不可恢复** |
---
### 改动已进入「暂存区」（已 `git add`，未 commit）
| 操作意图 | 命令 | 效果范围 |
| :--- | :--- | :--- |
| 撤销**单个文件**的暂存，改动保留在工作区 | `git restore --staged <file>` <br> 旧写法：`git reset HEAD <file>` | 对应文件暂存区 → 工作区清掉 |
| 撤销**所有文件**的暂存，改动全部保留在工作区 | `git restore --staged .` <br> 旧写法：`git reset HEAD .` | 暂存区 → 工作区 全部清空 |
| 撤销暂存 **且** 丢弃工作区改动（单个文件） | `git checkout HEAD -- <file>` <br> 新写法：`git restore --source=HEAD --staged --worktree <file>` | 对应文件暂存区 + 工作区清掉 |
| 撤销暂存 **且** 丢弃工作区改动（所有文件） | `git checkout HEAD -- .` <br> 新写法：`git restore --source=HEAD --staged --worktree .` | 暂存区 + 工作区 全部清空 |
---
### 改动已提交到「本地仓库」（已 commit，未 push）

`git reset` 的三种模式对比（以回退 1 个版本为例）：

| 模式 | 命令示例 | 提交历史 | 暂存区 | 工作区 |
| :--- | :--- | :--- | :--- | :--- |
| **--soft** | `git reset --soft HEAD~1` | 撤销 commit | ✅ 保留 | ✅ 保留 |
| **--mixed**（默认） | `git reset HEAD~1` | 撤销 commit | ❌ 清空 | ✅ 保留 |
| **--hard** | `git reset --hard HEAD~1` | 撤销 commit | ❌ 清空 | ❌ 清空 |
---
**典型场景对应：**

- **未提交到本地仓库的全量丢弃**：`git reset --hard HEAD`
- **提交错了分支，但想保留改动**：`git reset HEAD~1`（默认 --mixed）
- **彻底丢弃某个版本及之后所有改动**：`git reset --hard <commit-hash>`

**注意**：git reset --hard HEAD 和 git reset --hard HEAD~1不是一回事
虽然两者都会清空暂存区和工作区的改动，但前者执行命令后HEAD指针依旧指向最新的commit记录，而后者会撤销掉最新的commit，HEAD指针指向上一次commit记录

## 特定场景1:在已经提交到仓库，发现不得行，想丢掉这个版本，退回之前的版本(工作区未经修改的版本)
[命令]:git reset --hard xxxx
注:xxxx为版本代号，这个东西在输入git log --oneline查看日志命令后就能看到了
如:7f37a72 Target Press Key Up/Down make the number of items Correct
左边的一段码7f37a72，就是这个版本的代号
这个命令适用于本地开发，未推送到远程，执行后，彻底回退到你指定的版本代号，丢弃之前的版本的所有更改，然后之前版本的任何信息都会消失

## 特定场景2:用git reset命令重置了一个版本，突然后悔了
首先明确一件事，使用git reset --hard 版本代号，实际上仅移动分支指针指向旧提交，被重置版本的提交对象的提交对象仍存在于 .git/objects/ 中
[命令]:git reflog
查看 HEAD 移动历史（记录每次 HEAD 指向的 commit hash 就是 那个版本代号），只要这里可看到的版本代号，就能复原
找到你想要的版本后，用 git reset --hard 版本代号，就能恢复，但只能恢复那个版本的干净状态，要是你之前改了没提交的内容，依旧会消失，无法恢复

**注意**:reset 只是“移动指针”，不是物理删除
Git 的提交对象会保留 至少 30 天（默认），之后才可能被 git gc 清理
只要知道 commit hash（从 reflog 获取），就能 100% 恢复


# 待了解

##  .gitignore和.git
这东西能让git在add的时候忽略对应的东西，能有效实现仓库瘦身
要是仓库实在太大，要是提交记录分支什么的可以丢掉，那么直接删掉.git是最快的方法
.git文件夹其实就是Git的全部本体，所有版本、历史、分支全在这

## 版本号(Git Tag) 
git tag  = 给某个 commit 打上官方版本号标记(针对的是commit)
实现流程
```
第一步:打版本号标签
git tag v1.0.0
→ 就在你当前的代码状态，钉一个版本号
第二步:推送到云端（关键！）
git push origin v1.0.0
→ 把这个版本号传到 GitHub→ 不用写分支名
```
必须单独推 tag，版本号才会生效 
```
提醒
推代码 = 带分支名:git push origin main
推版本号 = 直接推 tag:git push origin v1.0.0
tag 不属于分支，所以不用写分支名
云端要看到版本号，必须单独推 tag
```
**文件版本是否为最新**
版本号为git判断文件是否为最新的首要依据(哪个数字大哪个就是最新的)，然后才是提交时间(提交顺序)，这个只有在无标签时生效。

## 分支合并

## 冲突解决

## 父仓库+子模块
这是仓库内含仓库自然而然遇到的内容，

# 遇到的问题
## 1
在WSL创建的文件夹，用命令初始化后，想要创建分支，但提示
fatal: detected dubious ownership in repository at '//wsl.localhost/Ubuntu-20.04/home/ubuntu/Project_Store/3_N498_OSD_SubMenu_V3'
这是一个 Git 安全机制引起的问题，表示 Git 检测到可疑的文件所有权。通常发生在以下情况:
问题原因
WSL2 与 Windows 文件系统交互:你正在通过 WSL2 访问位于 Windows 文件系统（/z/盘）中的 Git 仓库
文件所有权不一致:WSL 中的 Linux 用户 ID 与 Windows 文件系统中的文件所有者 ID 不匹配
Git 安全策略:Git 2.35+ 版本引入了更严格的所有权检查，防止潜在的安全风险
这时候根据它提示出的命令，直接复制黏贴即可

## 2
想回退到具体版本，但出现以下情况
 git reset --hard 9c496cd
Unlink of file 'NEW_BASE_20250732_NB.IAB' failed. Should I try again? (y/n) y
Unlink of file 'NEW_BASE_20250732_NB.IAB' failed. Should I try again? (y/n) y
这个大部分都是因为你已经打开项目文件，然后执行版本回退导致
解决方法:关掉当前项目相关的所有文件，然后重新执行回退

## 3
问题:直接将文件推送到暂存区后想直接git push却失败
xxxxxx@xxxxx MINGW64 /d/SpinOut (main)
git push
fatal: The current branch main has no upstream branch.
原因是:当前远程仓库没有设置上级，并且远程仓库的别名也不是origin，导致git不知道把文件往哪推
解决方法:给本地分支绑定一个“默认远程上级”
[命令]:git push -u 远程仓库别名(gitee/origin) 分支名
这样后就能直接用git push 推送东西了
注:但这个只是默认固定分支，要想推送不同的分支还得写详细的分支名
建议把主分支设置成默认固定分支
[命令]:git branch -vv
查看当前默认上级分支
输入命令后会显示
```
git branch -vv
* main b6b7697 [gitee/main] routine updates
这表示当前默认上级分支是以gitee为远程仓库别名的远程仓库的main分支
```

# 想不想知道
Q.将带有.git的文件夹整体复制到别处并命名为A,此时这个A是不是不用初始化仓库并带有以往的历史记录和分支？毕竟带上.git了
A:对，相当于本地完整镜像一份，和git clone起到的功能几乎完全一样，都是完整仓库，注意是完全和复制仓库一致的
包括分支，提交历史，链接远程仓库