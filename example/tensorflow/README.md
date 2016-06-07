# TensorFlow

Googleが出したDeep learningフレームワーク.

とりあえずネームバリューにより世界的な使用者が多い.
きっとにわかも多い.

## インストール

以下を見ればいいのだが.
https://www.tensorflow.org/versions/master/get_started/os_setup.html

一応簡単に入れるなら,以下で使えるようになる.

### Ubuntu
Python3.4と書いてあるがたぶん3.5でもいける.

CPUだけかGPUも使うかで,下のどちらかをinstall.

~~~
# Ubuntu/Linux 64-bit, CPU only, Python 3.4:
$ pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp34-cp34m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 3.4. Requires CUDA toolkit 7.5 and CuDNN v4.
# For other versions, see "Install from sources" below.
$ pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.8.0-cp34-cp34m-linux_x86_64.whl
~~~

### Mac OS X
~~~
# Mac OS X, CPU only:
$ pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/mac/tensorflow-0.8.0-py3-none-any.whl
~~~
