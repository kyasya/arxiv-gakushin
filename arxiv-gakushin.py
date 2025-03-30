#%%

import sys
import bibtexparser

if sys.version_info >= (3, 11):
    import tomllib as toml  # Python 3.11 以降は標準ライブラリを使用
else:
    import toml  # Python 3.10 以下では外部ライブラリ
    
class GakushinBiB:
    Filename = ''
    TomlfilePath = ''
    def __init__(self, filename='', tomlfilename='settings/sample.toml'):
        """
        GakushinBiBクラスのコンストラクタ
        :param filename: bibファイルのパス
        """ 
        self.LoadBiBFile(filename)
        self.LoadConfig(tomlfilename)

    def LoadBiBFile(self, filename):
        """
        bibファイルを読み込む
        :param filename: bibファイルのパス
        """
        if filename != '': self.Filename = filename
        with open(self.Filename, "r") as f:
            self.bibDB = bibtexparser.load(f)
    
    def LoadConfig(self, filename='settings/sample.toml'):
        """
        tomlファイルを読み込む
        :param filename: tomlファイルのパス
        """
        if filename != 'settings/sample.toml': self.TomlfilePath = filename
        with open(self.TomlfilePath, "r", encoding='utf-8') as f:
            self.TomlConfig = toml.load(f)

    def Analysis(self):
        """
        bibtexのエントリを解析する
        """
    
        # arXivのURLを取得
        for entry in self.bibDB.entries:
            # arXivのURLを取得
            # print(entry["url"])
            print(entry["title"])
            print(entry["author"])
            print(entry["year"])
            # print(entry["journal"])
            # print(entry["volume"])
            # print(entry["number"])
            # print(entry["pages"])
            # print(entry["doi"])
            # print(entry["publisher"])
            
            print(self.TomlConfig['MyName'])
            
            # 実際に処理する
            # entryのタグがあるか確認
            Counter = 0
            if entry['author']:
                Authors = entry.get('author').split(" and ")
                for author in Authors:
                    # print(author)
                    if author in self.TomlConfig['MyName']:
                        print("Found my name in author list.")
                        break
                    else:
                        Counter += 1
            Counter += 1
            print("All authors: {}, YourNo. {}".format(len(Authors), Counter))


if __name__ == "__main__":
    # # コマンドライン引数を取得
    # if len(sys.argv) != 2:
    #     print("Usage: python arxiv-gakushin.py <bibfile>")
    #     sys.exit(1)
    
    # bibファイルを読み込む
    BiB = GakushinBiB('./test.bib', './settings/mysettings.toml')
    BiB.Analysis()
