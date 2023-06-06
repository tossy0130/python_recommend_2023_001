import pandas as pd

############################ google, coraboratori で実践 ==========================

# csvデータ取得
df_review = pd.read_csv("./review.csv")
df_item = pd.read_csv("./item.csv")

# 先頭を出力 5行
df_review.head()

# 末尾を出力 5行 
df_item.tail()

# 詳細なデータを把握
### 出力結果 (46, 5)  ４６行の ５列　という意味
df_item.shape

### カテゴリー一覧出力
df_item["category"]

### 重複を除いたリストを抽出
df_item["category"].unique()

####### １行目の、 １～２１列目を :（スライス）で全て取得
df_review.iloc[:, 1:21]

df_review.head()

####### ２行目の、 １～２１列目を :（スライス）で全て取得
df_review.iloc[1, 1:21].values
