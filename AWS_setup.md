# Amazon Web Service メモ

ここはAWS EC2及びそのセットアップ周りの備忘録を記載する.

======
作成時の注意
pyenvとか結構容量食うのでHDD容量多めでインスタンスを作成する
足りなくなったら作り直そう

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

===============
Chromeのインストール

sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

sudo apt-get update

sudo apt-get install google-chrome-stable

chromeを立ち上げ、chromeのアプリストアからchromeリモートデスクトップをインストール

適当に設定するとchromeリモートデスクトップが使えるようになる…はず

https://support.google.com/chrome/answer/1649523?hl=ja

================

Eclipse+PyDevのインストール

sudo add-apt-repository ppa:webupd8team/java

sudo apt-get update

sudo apt-get install oracle-jdk7-installer



https://www.eclipse.org/downloads/download.php?file=/oomph/epp/mars/R2/eclipse-inst-linux64.tar.gz

からeclipseインストーラをダウンロード

cd ~/Download

tar -xvf eclipse-inst-linux64.tar.gz

cd eclipse-installer

./eclipse-inst

    Eclipse IDE for Java Developersを選択

    適当にすすめてインストール

eclipseを立ち上げて help->Install New Software

workwithへhttp://pydev.org/updates を入力-> add

ポップアップの名前はPyDevとでも

中央欄にチェックをつけてNext&accept&Finish




