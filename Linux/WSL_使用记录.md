WSL是一种实现在Windows下运行其他系统的技术，和VMware/VirtualBox不同，占用比其他两个都小

# WSL环境搭建

## 开启Windows子系统服务

打开控制面板-> 程序->程序和功能->启用或关闭Windows功能
勾选**适用于Linux的Windows子系统**和**虚拟机平台**，若有**Hyper-V**也勾选上

## 更新适用于x64计算机的WSL2 Linux内核

```
(Powershell)
wsl --update
```

## 终端设置WSL版本

```
(Powershell)
wsl --set-default-version 2
```

## 安装子系统

```
(Powershell)
wsl --install -d Ubuntu-20.04 --location D:\WSL\Ubuntu20_04
```

子系统终端下

## 更新软件源和已安装包

```
sudo apt update        # 更新本地软件包索引
sudo apt upgrade -y    # 升级所有已安装的软件包到最新版
```

## **安装基础编译工具**

```
sudo apt install -y git wget flex bison gperf cmake ninja-build ccache
```

## 安装python环境

```
# 1. 添加 deadsnakes PPA（一个专门提供新 Python 版本的第三方源）
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# 2. 安装 Python 3.12 以及它的 venv、pip（pip 一般会用 ensurepip 自动装）
sudo apt install -y python3.12 python3.12-venv python3.12-dev
```

# 查看WSL信息

Powershell下运行
1.查看当前已安装的子系统

```
WSL --list --verbose
```

2.查看当前子系统数据盘的位置
首先要先知道子系统的名字，运行1可知

```
wsl --shutdown  # 先关闭 WSL，避免文件被占用

命令参数根据子系统名字不同而不同，下面是通用版(黏贴后回车运行即可)
Get-ChildItem HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss | ForEach-Object {
    $distro = Get-ItemProperty $_.PSPath
    Write-Host "发行版：$($distro.DistributionName)"
    Write-Host "真实路径：$($distro.BasePath)"
}
```
3.子系统数据盘安装位置
如果是在微软商店下载的子系统如Ubuntu，那么默认数据盘会在C盘，这时候需要自己把数据迁移到其他盘，
还有记得在应用管理，搜索ubuntu将安装位置移动到D盘，这个ubuntu指的是应用商店中ubuntu的本体

4.建议用命令安装子系统
记得提前创建好文件夹

```
wsl --install -d Ubuntu-20.04 --location D:\WSL\Ubuntu20_04
```

5.查看Linux版本

```
# 简洁版
lsb_release -a
# 查看内核版本
uname -a
```

6.更新软件源和已安装的数据包

```
sudo apt update        # 更新本地软件包索引
sudo apt upgrade -y    # 升级所有已安装的软件包到最新版
```

