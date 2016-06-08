# Amazon Web Service メモ

ここはAWS EC2及びそのセットアップ周りの備忘録を記載する.

======
CUIアクセス

```
ssh -i ~/.ssh/XXXX.pem ubuntu@xxxxx # ダウンロードしたsshキーXXX.pemとサーバー名xxxxxを指定
```

=======
VNCアクセス
サーバー上の設定

```
sudo apt-get update
sudo apt-get install ubuntu-desktop
sudo apt-get install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
sudo apt-get install vnc4server
vncserver
vncserver -kill :1
vim ~/.vnc/xstartup

####################################
# ~/.vnc/xstartup
#!/bin/sh
export XKL_XMODMAP_DISABLE=1
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey
vncconfig -iconic &

gnome-panel &
gnome-settings-daemon &
metacity &
nautilus &
gnome-terminal &
######################################

vncserver
```
 - クライアントからアクセス
SSHトンネルを作成

```
ssh -L 5901:localhost:5901 -i ~/.ssh/XXXX.pem ubuntu@xxxxx
````

VNC viewerから localhost:1

