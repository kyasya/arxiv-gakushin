# bib-gakushin

![](./docs/img/bib-gakushin.png){width=500}

[![MIT](https://custom-icon-badges.herokuapp.com/badge/license-MIT-8BB80A.svg?logo=law&logoColor=white)](LICENSE)
[![Python](https://custom-icon-badges.herokuapp.com/badge/Python-3572A5.svg?logo=Python&logoColor=white)]()
[![Windows](https://custom-icon-badges.herokuapp.com/badge/Windows-1BB2E4.svg?logo=Windows&logoColor=white)]()
[![Linux](https://custom-icon-badges.herokuapp.com/badge/Linux-F6CE18.svg?logo=Linux&logoColor=white)]()
[![](https://img.shields.io/badge/version-b.1.0.0-blue.svg)]()

学振書くときに使えるやつ。

自分の番号が何番目か書くのがめんどくさいので自分の主著、共著論文をまとめたbibリストを作っておけば読み込めるようにした。

- リリース情報
	- b.1.0.0(最新): 超最低限の機能[リリース情報](#b100)

- 今後のアップデート方針
	- 次のバージョン: v1.0.0
	- 最低限のフォーマットに対応する
	- 文献の省略表記を自動化する

## Install

cloneするだけ

```bash
git clone https://github.com/kyasya/bib-gakushin.git
```

必要なパッケージ

- bibtexparser

一括でインストールできる(まだ一つしかないけど今後増えるかもしれないので)

```bash
pip install -r requirements.txt
```

## 使い方/注意

1. settingsにあるコンフィグファイル`sample.toml`をコピーし(コードでは`mysettings.toml`としている)、中にある`MyName`パラメータに自分の名前を日本語、英語両方で書く。
   1. 場合によっては`bib-gakushin.py`中にあるコンストラクタを変更する。第一引数は`bibファイル`のパス(./test.bib)、第二引数が`コンフィグファイル`のパスである。
2. あとは普通に実行。

```bash
python bib-gakushin.py
```

NOTE: これはあくまで補助。現状表記揺れ等には対応していない。

## リリース情報

### b1.0.0

初期のアップデート。

- **最低限の機能の実装**
	- 自分の名前が何人目かわかる。

## ライセンス

[MIT License](LICENSE)
