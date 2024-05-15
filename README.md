# HBUT-automatically-connect-to-campus-network
自动连接湖北工业大学校园网的一个小脚本

#### 下面是步骤
1. 下载对应浏览器相应版本的WebDrive
例如我的chrome版本就是124开头的，就去https://googlechromelabs.github.io/chrome-for-testing/里去找对应的版本的WebDrive

![image](https://github.com/lila233/HBUT-automatically-connect-to-campus-network/assets/114989021/b50e3c38-c0a7-4215-8900-24380620bbc8)

下载相应的系统版本的即可

![image](https://github.com/lila233/HBUT-automatically-connect-to-campus-network/assets/114989021/908dd6d7-f7c1-4285-8467-8bab90b57918)

自己选择解压缩路径，等会脚本里会用到

3. 将脚本内容替换为自己的信息
一共有四个地方需要修改，分别对应着校园网登录时的用户名，密码和运营商
![image](https://github.com/lila233/HBUT-automatically-connect-to-campus-network/assets/114989021/f847ba04-b350-4ab2-a1bb-4c07f3caff3f)

还剩下一个是你刚刚解压缩的chromedrive.exe的路径

3. 开机自启动
在C:\Users\xxxx\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup (xxxx为你自己的用户名，注意一下其中里面的user，programs等目录可能会按照你系统的语言进行本地化）路径下创建一个txt文件内容为


    @echo off
    python xxxxxx


其中xxxxxx为py脚本的具体地址
然后将其后缀改为.bat即可在开机后自动运行你的python脚本了
