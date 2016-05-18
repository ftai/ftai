# Ubuntuの設定に関する備忘録

ググれば出るが一覧性が悪いのでここに記載.

日本ロケール
~~~
sudo aptitude install language-pack-ja-base language-pack-ja ibus-mozc
sudo update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja"
source /etc/default/locale
~~~

設定から日本語キーボード、日本語入力を設定すればOK.

Git
~~~
sudo apt-get install git
~~~
