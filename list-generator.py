#%%

import sys
import bibtexparser

if sys.version_info >= (3, 11):
	import tomllib as toml  # Python 3.11 以降は標準ライブラリを使用
else:
	import toml  # Python 3.10 以下では外部ライブラリ

import pandas as pd
from IPython.display import display

class ListGenerator:
	TomlConfigPath = ''
	PaperListPath = ''
	TalkListPath = ''
	def __init__(self, tomlfilename='settings/sample.toml'):
		"""
		コンストラクタ
		:param filename: ファイルのパス
		""" 
		# self.LoadBiBFile(filename)
		# self.LoadConfig(tomlfilename)

	def LoadSettings(self, filepath=''):
		if filepath != '': self.TomlConfigPath = filepath

		with open(self.TomlConfigPath, 'r') as f:
			Toml = toml.loads(f)
			pass

	def LoadListCSV(self, filename, output_filepath):
		"""
		CSVリストを読み込む
		:param filename: ファイルのパス
		"""
		if filename != '': self.Filename = filename
		with open(self.Filename, "r") as f:
			self.bibDB = bibtexparser.load(f)

	def ReplaceString(self, string:str):
		Table = {
			'#':'\\#',
			'〜':'$\\sim$',
			'ポスター':'ポスター発表'
		}
		for old, new in Table.items():
			string.replace(old, new)
		return string

	def ReplaceReference(self, string:str):
		Table = {
      		'International Cosmic Ray Conference':'ICRC',
			'Topics in Astroparticle and Underground Physics':'TAUP'
		}
		for old, new in Table.items():
			string.replace(old, new)
		return string


	def GeneratePaperList(self, filepath='./paper-list.csv', output_filepath='paper-list.txt'):
		if filepath != '': self.PaperListPath = filepath

		df = pd.read_csv(self.PaperListPath, encoding='utf-8')
		df = df.drop(['リンク', 'メモ'], axis=1)
		df = df.fillna('')

		# display(df)
		with open(output_filepath, 'w', encoding='utf-8') as f:
			for index, row in df.iterrows():

				# 名前
				Name=  row[0] 
				if int(row[2]) > 1: Name +=" \\etal" # 一人だけじゃないとき

				if int(row[1]) == 1: Name += " {\\bf (筆頭著者)}"
				else:				 Name += f"(先頭から{row[1]}番目)"

				Result = '\\paper{'+Name+'}' # 名前
				Result += '{'+row[3]+'}' # タイトル
				Journal = self.ReplaceReference(row[4])
				Result += '{'+Journal+'}' # 掲載誌
				Result += '{'+row[5]+'}' # 巻数
				Result += '{'+row[6]+'}' # ページ

				dt = pd.to_datetime(row[7])
				Result += '{'+f'{dt.year}'+'}'

				Result += '\n'
				f.write(Result)

	def GenerateTalkList(self, filepath='./talk-list.csv', output_filepath='talk-list.txt'):
		if filepath != '': self.TalkListPath = filepath

		df = pd.read_csv(self.TalkListPath, encoding='utf-8')
		df = df.drop(['リンク', 'メモ'], axis=1)
		df = df.fillna('')

		# display(df)
		with open(output_filepath, 'w', encoding='utf-8') as f:
			for index, row in df.iterrows():
				Result = '\\talk{'+row[5]+'}' # 名前
				Result += '{'+row[6]+'}' # タイトル
				Journal = self.ReplaceReference(row[3])
				Result += '{'+Journal+'}' # 学会名
				Result += '{'+row[7]+'}' # 場所

				dt = pd.to_datetime(row[0])
				Result += '{'+f'{dt.year}年{dt.month}月'+'}'

				if row[4] == '招待講演': Result += '{\\bf 招待講演}'
				else: 					Result += '{'+row[4]+'}'

				Result += '\n'

				# 文字列の置換

				f.write(self.ReplaceString(Result))

	def GenerateAwardList(self, filepath='./award-list.csv', output_filepath='award-list.txt'):
		if filepath != '': self.TalkListPath = filepath

		df = pd.read_csv(self.TalkListPath, encoding='utf-8')
		df = df.drop(['リンク', 'メモ'], axis=1)
		df = df.fillna('')

		# display(df)
		with open(output_filepath, 'w', encoding='utf-8') as f:
			for index, row in df.iterrows():
				sThisRef = ''

				sThisRef += ' '+row[1] # 項目

				dt = pd.to_datetime(row[0])
				sThisRef += f' ({dt.year}年{dt.month}月)'


				sThisRef += '\n'
				f.write(sThisRef)

if __name__ == "__main__":
	# # コマンドライン引数を取得
	# if len(sys.argv) != 2:
	#     print("Usage: python arxiv-gakushin.py <bibfile>")
	#     sys.exit(1)

	# bibファイルを読み込む
	ListGen = ListGenerator('./settings/mysettings.toml')
	# ListGen.GeneratePaperList()
	ListGen.GenerateTalkList()
	# ListGen.GenerateAwardList()
