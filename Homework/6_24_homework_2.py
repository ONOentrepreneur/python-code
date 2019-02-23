"""
[[1, '英語', 25], [1, '国語', 63], [1, '数学', 42], [2, '地歴', 90], [2, '英語', 44], [3, '数学', 94]]
のような番号、教科、点数からなるリストが与えられます。
以下の二つの方法で教科ごとの平均点と最高点、最低点、番号ごとの平均点を求めるプログラムを作成してください

1. Pythonの標準モジュールのみを利用して作成してください
2. pandasモジュールを利用してプログラムを作成してください

pandasはpipもしくはcondaを利用してインストールできます(Anacondaをインストールして方はすでにインストールされています)。
pandasはデータを集計したり解析したりするためのモジュールです。
"""
#1
import pandas as pd
df=pd.DataFrame([[1, '英語', 25], [1, '国語', 63], [1, '数学', 42], [2, '地歴', 90], [2, '英語', 44], [3, '数学', 94]],columns=['number','subject','score'])
#print(df)
#print(df['subject'])
#av_1=df.groupby('subject').mean()
#print(av['score'])
print('--平均点--')
print(df.groupby('subject').mean()['score'])
#print(df['subject'][1])
print('--最高点--')
print(df.groupby('subject').max()['score'])
print('--最低点--')
print(df.groupby('subject').min()['score'])

#2
#av_2=df.groupby('number')
print('--平均点--')
print(df.groupby('number').mean()['score'])
