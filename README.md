# AllServer -Server-

AllServerについての基本的な情報は[ここ](https://github.com/stsaria/allserver)から

## 目次
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [必要環境](#%E5%BF%85%E8%A6%81%E7%92%B0%E5%A2%83)
- [引数](#%E5%BC%95%E6%95%B0)
- [インストール方法](#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)
- [サーバーの使い方](#%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9)
  - [マインクラフトサーバー](#%E3%83%9E%E3%82%A4%E3%83%B3%E3%82%AF%E3%83%A9%E3%83%95%E3%83%88%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC)
    - [特別必要要件](#%E7%89%B9%E5%88%A5%E5%BF%85%E8%A6%81%E8%A6%81%E4%BB%B6)
    - [サーバーをリストサーバーに登録](#%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%82%92%E3%83%AA%E3%82%B9%E3%83%88%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%81%AB%E7%99%BB%E9%8C%B2)
    - [サーバー起動](#%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E8%B5%B7%E5%8B%95)
  - [リストサーバー](#%E3%83%AA%E3%82%B9%E3%83%88%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC)
    - [特別必要要件](#%E7%89%B9%E5%88%A5%E5%BF%85%E8%A6%81%E8%A6%81%E4%BB%B6-1)
    - [サーバー起動](#%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E8%B5%B7%E5%8B%95-1)
  - [自動起動設定](#%E8%87%AA%E5%8B%95%E8%B5%B7%E5%8B%95%E8%A8%AD%E5%AE%9A)
    - [特別必要要件](#%E7%89%B9%E5%88%A5%E5%BF%85%E8%A6%81%E8%A6%81%E4%BB%B6-2)
    - [設定](#%E8%A8%AD%E5%AE%9A)
- [iniファイル](#ini%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)
  - [iniファイルとは](#ini%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%A8%E3%81%AF)
  - [ファイル一覧](#%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E4%B8%80%E8%A6%A7)
- [言語ファイル](#%E8%A8%80%E8%AA%9E%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)
  - [言語ファイルとは](#%E8%A8%80%E8%AA%9E%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%A8%E3%81%AF)
  - [作成・記述方法](#%E4%BD%9C%E6%88%90%E3%83%BB%E8%A8%98%E8%BF%B0%E6%96%B9%E6%B3%95)
  - [読み込み方法](#%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF%E6%96%B9%E6%B3%95)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 必要環境
- OS Linux/Windows
- Java(Minecraftバージョンに合っている)(クライアントモードの場合は必要なし)
- Python3(最新バージョン推奨)(バイナリの場合は必要なし？)<br/>
  Requests(ライブラリ)
## 引数
※ 初めての方はこれを飛ばして操作方法を見てください<br/>
Systemdやスタートアップなどで起動する際に使用できます
- `--help` ヘルプを表示 `python3 allserver.py --help`

- `--search/serverip` サーバーを検索 `python3 allserver.py --search`
    追加引数
    - `--plus-not-lang` 設定言語(国名)以外のサーバーも検索  `python3 allserver.py --search/serverip --plus-not-lang`
    - `--plus-not-team` 設定チーム以外のサーバーも検索  `python3 allserver.py --search/serverip --plus-not-team`

- `--start-minecraft-server`　マインクラフトサーバーを起動（待機）`python3 allserver.py --start-minecraft-server`

- `--start-list-server` リストサーバーを起動 `python3 allserver.py --start-list-server`

- `--build` ソースコードをビルド (Pyinstallerが必要・バイナリの場合は不可) `python3 allserver.py --build`
## インストール方法
1. pipでライブラリをインストールする。
もし、pipが入ってない場合はパッケージ管理システムなどで入れてください。
```
pip install -r requirements.txt
```
2. インストール先が正しくパーミッション・所有者が設定されていることを確認してください。<br/>
Linux : `ls -l`<br/>
Windows : `dir /q`
3. <a href="https://github.com/stsaria/allserver/releases">ダウンロード</a>からバイナリをダウンロードします<br/>
もし、何らかの問題でバイナリが実行できない場合は、<a href="https://github.com/stsaria/allserver/archive/refs/heads/main.zip">ダウンロード</a>からソースコードをダウンロードします。
```
git clone https://github.com/stsaria/allserver.git
```
4. もしZipやGztarなどの場合はファイルを解凍します。
5. allserver.pyを起動します<br/>
('--help'引数を使えばヘルプが出ます)
```
python3 allserver.py

AllServer

モードを選択してください。

[1] : マインクラフトサーバーモード（サーバー支援・リストに登録）
[2] : リストサーバーモード（マインクラフトサーバーリスト）
[3] : 自動起動設定モード
[4] : 終了
[1,2,3,4] :
```
## サーバーの使い方
### マインクラフトサーバー
#### 特別必要要件
- 固定グローバルIP<br/>
  Q:なぜ固定グローバーIPにする必要がありますか？<br/>
  A:リストサーバーに登録する際に使われているIPを、そのまま使うシステムであることが原因です。<br/>
  (ただし、リストサーバーを使わない場合は、絶対必要ではありません。)<br/>
- ポート**50385**の開放
- メモリ容量2GB以上(推奨4GB以上)
#### サーバーをリストサーバーに登録
公式リストサーバー:st-allserver.f5.si
1. allserver.pyを起動
2. マインクラフトサーバーモードを選択
3. サーバー登録モードを選択
4. リストサーバーのIPを入力
5. サーバー名、補足を入力
```
python3 -u allserver.py
AllServer

モードを選択してください。

[1] : マインクラフトサーバーモード（サーバー支援・リストに登録）
[2] : リストサーバーモード（マインクラフトサーバーリスト）
[3] : 自動起動設定モード
[4] : 終了
[1,2,3,4] :1
マインクラフトサーバーモードを選択してください。

[1] : サーバー起動
[2] : サーバー登録(リストサーバー)
[3] : 戻る
[1,2,3] :2
サーバーIPを入力してください :サーバーIP
サーバー名を入力してください :マインクラフト1
補足を入力してください :message
成功しました
```
※リストサーバーとマインクラフトサーバーが同じコンピューター内にある場合は"127.0.0.1"のようなIPになってしまいます。<br/>
同じく両サーバーがローカルなネットワークにある場合は、ローカルなIPになります。
#### サーバー起動
1. allserver.pyを起動
2. マインクラフトサーバーモードを選択
3. サーバー起動モードを選択
[server.properties.template](config/server.properties)(サーバー設定テンプレート)に基本的なサーバーの設定を書き込むことができます。（サーバーポート・サーバー名は変更できません）<br/>
ただし、記述方法が間違っている場合は正しく起動できない可能性があります。
```
python3 -u allserver.py   
AllServer

モードを選択してください。

[1] : マインクラフトサーバーモード（サーバー支援・リストに登録）
[2] : リストサーバーモード（マインクラフトサーバーリスト）
[3] : 自動起動設定モード
[4] : 終了
[1,2,3,4] :1
マインクラフトサーバーモードを選択してください。

[1] : サーバー起動
[2] : サーバー登録(リストサーバー)
[3] : 戻る
[1,2,3] :1
yyyy-mm-dd hh:mm:ss,fff@ Start Server
CtrlとCを押せば終了します
```
引数で起動する場合(Systemd・スタートアップ等)は`--start-minecraft-server`引数をallserver.pyの後につけて起動する
```
python3 -u allserver.py --start-minecraft-server
AllServer

yyyy-mm-dd hh:mm:ss,fff@ Start Server
CtrlとCを押せば終了します
```
### リストサーバー
#### 特別必要要件
- ポート**50384**の開放
#### サーバー起動
1. allserver.pyを起動
2. リストサーバーモードを選択
3. サーバー起動モードを選択<br/>
※初回起動時には説明が出ます
```
python3 -u allserver.py
AllServer

モードを選択してください。

[1] : マインクラフトサーバーモード（サーバー支援・リストに登録）
[2] : リストサーバーモード（マインクラフトサーバーリスト）
[3] : 自動起動設定モード
[4] : 終了
[1,2,3,4] :2
あなたはこのリストサーバーを立てるのは初めてですか？
注意事項があります。
・ローカル内以外に公開する場合はTCPポート 50384 をルーターなどで開放してください。
・logフォルダーのlistserver.logにIP情報を含むログが記録されています。
もし常識的なアクセス数を超える場合(いわいる、'DOS'というもの)は、IPをブロックするといいでしょう。

作成しますか？
[1] : 作成する
[2] : 戻る
[1,2] :1
yyyy-mm-dd hh:mm:ss,fff@ Start Server
CtrlとCを押せば終了します
```
引数で起動する場合(Systemd・スタートアップ等)は`--start-list-server`引数をallserver.pyの後につけて起動する
```
python3 -u allserver.py --start-list-server
AllServer

yyyy-mm-dd hh:mm:ss,fff@ Start Server
CtrlとCを押せば終了します
```
### 自動起動設定
#### 特別必要要件
- 管理者権限が必要
- Linuxの場合はSystemdの導入が必要
#### 設定
1. allserver.pyを管理者で起動
2. 自動起動設定モードを選択
3. マインクラフトサーバーかリストサーバーを選択
```
python -u allserver.py
AllServer

モードを選択してください。

[1] : マインクラフトサーバーモード（サーバー支援・リストに登録）
[2] : リストサーバーモード（マインクラフトサーバーリスト）
[3] : 自動起動設定モード
[4] : 終了
[1,2,3,4] :3
自動起動するサーバーを選択してください。
※Linuxをお使いの場合はSystemdが導入されていることを確認してください。

[1] : マインクラフトサーバー
[2] : リストサーバー
[3] : 終了
[1,2,3] :1 または 2
成功しました
```