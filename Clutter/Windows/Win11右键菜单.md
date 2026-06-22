Win11右键菜单设置
若嫌右键菜单选项过多，下载官方的Autoruns注册表管理器,来对症下药

想恢复Win10的右键菜单风格？
打开 Windows 终端 (管理员) / 命令提示符 (管理员)
复制粘贴下面命令，回车执行：
```
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f
```
然后重启资源管理器->打开任务管理器，找到Windows资源管理器->右键重启
若想恢复，同样流程执行一次
```
reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f
```
