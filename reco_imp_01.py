import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

############################ google, coraboratori で実践 ==========================

### sklearn を使って、学習、推論、出力する

# === .csv 読み込み
df_review = pd.read_csv("./review.csv")
df_item = pd.read_csv("./item.csv")

df_review.head()

### データ取得
X_train = df_review.iloc[:, 1:]

### 学習
nn = NearestNeighbors(n_neighbors=3, metric= 'cosine')
model_nn = nn.fit(X_train.values)

### 出力  初心者Ruby 取得
ruby_for_beginner = df_review.iloc[0, 1:]

### 推論　出力　出力結果：array([[ 0,  2, 11]])
model_nn.kneighbors(ruby_for_beginner.values.reshape(1, -1))[1]

### 推論取得データ出力
df_review.iloc[2]["book"]
df_review.iloc[11]["book"]
