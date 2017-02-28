## このリポジトリの概要
* pythonに関するCI環境のサンプル。



## テストのディスカバリ実行
* cd (プロジェクトの最上位ディレクトリ)
* python3 -m unittest discover --verbose

## カバレッジの測定
* カバレッジの計測
  * cd (プロジェクトの最上位ディレクトリ)
  * coverage run -m unittest discover
* htmlに変換
  * coverage html

## 今後のTODO
* カバレッジの測定
  * 不要なディレクトリ、ソースファイルを除外する方法
* mockライブラリを使ってみる
  * 公式よりも、以下URLの方がとっつきやすそう。
  * [まだmockで消耗してるの？mockを理解するための3つのポイント](http://note.crohaco.net/2015/python-mock/)

## 参考
### ユニットテストに関して
* [26.4. unittest — ユニットテストフレームワーク](http://docs.python.jp/3/library/unittest.html)
  * 公式ドキュメント。
* [Running unittest with typical test directory structure](http://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure)
  * StackOverFlowの記事。
  * テストクラス群を独立したディレクトリで管理する場合の、テスト実行方法。
  * 以下が参考になった。
    * テスト対象ソースや、テストクラスは、__init__.pyを使ってパッケージ化する。
    * プロジェクトの最上位ディレクトリに移動してテスト実行する。
* [Coverage.py](https://coverage.readthedocs.io/en/coverage-4.3.4/index.html)
  * 公式ドキュメント
* [車窓からのTDD](http://objectclub.jp/technicaldoc/testing/stack_tdd.pdf)
  * サンプルの一部は、上記PDFを参考にした。
* [testfixturesライブラリ](https://testfixtures.readthedocs.io/en/latest/)
  * 以下のようなテストができる、便利ライブラリ。
  * テスト時に困った際は、必要に応じて学習してみよう。
    * オブジェクトの便利な比較。
    * オブジェクトのモック。
    * システム日付を差し替える。
    * ファイルIOなどの副作用を伴う処理のテスト。