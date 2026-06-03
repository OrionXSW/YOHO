WSL是一种实现在Windows下运行其他系统的技术，和VMware/VirtualBox不同

以下命令均在PowerShell下运行
1. 查看当前已安装的子系统
```
WSL --list --verbose
```

2. 查看当前子系统数据盘的位置
首先要先知道子系统的名字，运行1可知
```
wsl --shutdown  # 先关闭 WSL，避免文件被占用

命令参数根据子系统名字不同而不同，下面是通用版
Get-ChildItem HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss | ForEach-Object {
    $distro = Get-ItemProperty $_.PSPath
    Write-Host "发行版：$($distro.DistributionName)"
    Write-Host "真实路径：$($distro.BasePath)"
}
```
3. 子系统数据盘安装位置
如果是在微软商店下载的子系统如Ubuntu，那么默认数据盘会在C盘，这时候需要自己把数据迁移到其他盘，