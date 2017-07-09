# -*- coding: utf-8 -*-
"""testfixturesライブラリによる、ファイルIO処理のテスト例。
簡単のため、ファイル内にテスト対象の関数も含めている。"""
import os
import unittest
from pprint import pprint

from testfixtures import TempDirectory


# 以下のような、ファイルを扱う関数をテスト対象にしてみる。
def replace_file_contents(dirpath, filename, before, after):
    """テキストファイル中の、特定文字列を置き換える。"""
    path = os.path.join(dirpath, filename)
    with open(path, 'r') as input:
        contents = input.read()
    contents = contents.replace(before, after)
    with open(path, 'w') as output:
        output.write(contents)


class FileIOTest(unittest.TestCase):
    """ファイルIOの副作用を持つ処理のテスト例。"""

    def tearDown(self):
        # 以下メソッドは、テストケース終了時に、必ず呼んでしまって構わないようだ。
        TempDirectory.cleanup_all()

    def test_replace_file_contents(self):
        """ファイルの文字列を書き換える関数のテスト。"""
        # ファイルやディレクトリのテストでは、まず以下インスタンスを生成する。
        temp_dir = TempDirectory()

        # writeメソッドで、ファイル作成できる(以下のように、存在しないディレクトリも再帰的に作ってくれる)。
        # 一点注意すべきなのが、デフォルトだとbyte文字列しか書き込みできないこと。
        # 通常の文字列を書き込みたい場合、エンコーディングの指定が必須。
        # http://testfixtures.readthedocs.io/en/latest/api.html
        temp_file = temp_dir.write('foo/bar/sample.txt', 'I love cat.\nMy cat\'s name is mike.\n', encoding='utf-8')

        # テストケース実施
        replace_file_contents(temp_dir.path + '/foo/bar', 'sample.txt', 'cat', 'dog')

        # ファイルの結果を確認する。
        self.assertEqual(
            'I love dog.\nMy dog\'s name is mike.\n',
            # readメソッド呼び出し時にも、エンコーディングの指定が要るので注意(省略した場合はバイト文字列)。
            temp_dir.read('foo/bar/sample.txt', encoding='utf-8')
        )

        # 以下を呼ぶことで、ディレクトリ以下の内容を再帰的にcleanしてくれる。
        temp_dir.cleanup()
