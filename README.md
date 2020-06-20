# make-plymouth-theme

### 概要
これは、plymouthのループするスプラッシュテーマを作成するPythonスクリプトです。

### 必要なパッケージ

~~~
Python3.3以降
ffmpeg
~~~

### 使い方
~~~
chmod u+x mkplymouth.py
./mkplymouth.py ビデオファイル名 テーマ名
~~~

ビデオファイル名にはPlymouthテーマに変換したい動画ファイルを、テーマ名には変換後のPlymouthテーマの名前を入力して下さい。

実行するとテーマ名と同じディレクトリが出来るのでそれを/usr/share/plymouth/themes辺りに移動してテーマを適用して下さい。
