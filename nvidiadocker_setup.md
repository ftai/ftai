# AWS上でNvidia-dockerを使ってみるためのメモ


とりあえず,ググったり本呼んだりしながら、なんとか環境構築できたので
その過程をメモったものです.マサカリ大歓迎です＼(^o^)／

## TODO
 1. 他のライブラリやマシン環境に対応したDockerfileの準備.
 2. AWSのインスタンス時間の自動管理.  

## AWS環境構築
（手持ちのマシンにGPUが載っている場合,ここはスキップしてよい）

この辺は, "プログラマのためのDockerの教科書"の７章を参考にした.

手順
1. AWSにアカウントを作る.
  1. アカウントを作る.
  2. AWSからIAMを選択.そこでユーザ設定を行い,アクセスキーIDとシークレットアクセスキーをメモる.
  3. ポリシーのアタッチ画面で, AmazonEC2FullAcessを選択する.
  4. AWSサービスからVPCを選択.IDをメモる.
  5. 今回,AWSのGPUマシンの内,g2.2xlargeとインスタンスを使用する.
     インスタンスの利用制限が最初から0となっているので、追加申請を行う.
     場所はEC2ダッシュボードの制限タブから行ける.

2. DockerMachineをインストール.
[本家](https://docs.docker.com/machine/install-machine/)
から.

3. DockerMachineのコマンドを使って, AWSにDockerホストを構築.
```
docker-machine create \
  --driver amazonec2 \
  --amazonec2-ami ami-d732f0b7 \ #マシンイメージ(注意１）
  --amazonec2-region us-west-2  \ #リージョンの指定(注意２）
  --amazonec2-instance-type g2.2xlarge \ #インスタンスの指定
  --amazonec2-vpc-id vpc-******** \ #vpc-idの指定
  --amazonec2-access-key *********** \ # アクセスキーID
  --amazonec2-secret-key *********** \ # シークレットアクセスキー
  aws01 #インスタンス名前
```
注意1: AMIはインスタンス生成に必要なソフトウエア構成(OS等)のテンプレート. 最初,何も指定しなかったら,
ubuntuの最新版(15系?)だった. dockerhubのnvidia-dockerのページを見ても対応しているのは14.04までだったので,
そのイメージを指定した.

注意２: どこがいいのか知らないが、オレゴンのほうが安いらしい.

このコマンドで上手くいったのなら、AWSのサイト上でもインスタンスが生成されているのが
確認できるはず.

以下, よく使うコマンド.
```
docker-machine run aws01 # 走らせる
docker-machine ssh aws01 # リモートに入る.
docker-machine stop aws01 # 止める
docker-machine rm aws01 # 消す.
```

もし,すぐ使用しないなら,ちゃんと切っておいたほうがよい.
*私は２つのインスタンスをrunした状態で2日放置しておいたら,40$
くらい請求来た.*


## dockr環境の構築.

参考にしたのは,[1](http://qiita.com/mana-murakami/items/2ff0c3b3ecd4ce85c2cd),[2](https://docs.docker.com/cs-engine/install/#/install-on-ubuntu-14-04-lts ),[3](http://www.muo.jp/2016/05/nvidia-docker-tensorflow.html).のブログ.

[1](http://www.slideshare.net/unnonouno/chainerdockercuda),[2](http://www.slideshare.net/yutakashino/chainer-meetup2016-0702)はnvidia-dockerが必要な理由を紹介してくれている.

以下の操作は, リモート環境で行う.
```
docker-machine ssh aws01  
```
1. NVIDIA Driverのインストール

  1. まず,最低限の環境をインストール.
  ```
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install build-essential
  ```
  2. リポジトリを追加,　アップデート
  ```
   sudo add-apt-repository ppa:graphics-drivers/ppa
   sudo apt-get update
  ```
  3. インストール可能なドライバの表示.
  ```
   sudo apt-cache search nvidia-\d+
  ```
  4. 表示されたドライバをインストール.
   とりあえず、一番最新を選択.
   ```
   sudo apt-get install nvidia-367
   sudo apt-get install nvidia-modprobe
   ```
  5. 再起動.
  ```
   sudo reboot
  ```
  6. 確認.
  ```
   sudo nvida-smi
  ```

2. Dockerのインストール
  公式に従う.
  ```
  curl -s 'https://sks-keyservers.net/pks/lookup?op=get&search=0xee6d536cf7dc86e2d7d56f59a178ac6c6238f52e' | sudo apt-key add --import
  sudo apt-get update && sudo apt-get install apt-transport-https
  sudo apt-get install -y linux-image-extra-virtual
  echo "deb https://packages.docker.com/1.11/apt/repo ubuntu-trusty main" | sudo tee /etc/apt/sources.list.d/docker.list
  sudo apt-get update && sudo apt-get install docker-engine
  sudo docker info
  sudo reboot
  ```
3. nvidiaDockerのインストール
```
  wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.0-rc/nvidia-docker_1.0.0.rc-1_amd64.deb
  sudo dpkg -i /tmp/nvidia-docker_1.0.0.rc-1_amd64.deb && rm /tmp/nvidia-docker*.deb
```
4. Dockerfileの作成.
  以下のような雛形を作る.
  ```
  Dockerfileを~/docker/tensorflow/Dockerfileで作成.
  FROM nvidia/cuda:7.5-cudnn5-devel
  RUN apt-get update \
   && apt-get install -y --no-install-recommends python-pip python-dev \
   && pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl \
   && rm -rf /var/lib/apt/lists/*
  RUN ln -s /usr/local/nvidia/lib64/libcuda.so.1 /usr/lib/x86_64-linux-gnu/libcuda.so
```
5. 実行.
  Dockerfileのあるディレクトリで, build.
```
  sudo docker build -t local:tf .

  sudo nvidia-docker run --rm -it local:tf /bin/bash
 ```
注意:
  Dockerfileは作らなくても, Dockerhubというサイトで公開されており、
  以下のコマンドから取得できる.
  ```
  docker pull ww24/deep-learning
  ```
  また、chainer, caffe等の全部入りがある.
  ```
  docker pull ww24/deep-learning
  ```
  [1](http://www.slideshare.net/ww24jp/docker-deep-learning),  [2](http://www.slideshare.net/yutakashino/chainer-meetup2016-0702)のスライドが参考になる.
  ただし、上記における環境での動作確認はしていない.
  また,エラーについては[ここ](http://www.kabuku.co.jp/developers/errors-with-tensorflow-on-gpu)に詳しい.
