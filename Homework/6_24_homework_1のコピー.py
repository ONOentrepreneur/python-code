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
score_list = [[1, '英語', 25], [1, '国語', 63], [1, '数学', 42], [2, '地歴', 90], [2, '英語', 44], [3, '数学', 94]]
sub_ave_dic={}
count_dic={}
for x in score_list:
    if x[1] in sub_ave_dic:
        sub_ave_dic[x[1]]+=x[2]
        count_dic[x[1]]+=1
    else:
        sub_ave_dic[x[1]]=x[2]
        count_dic[x[1]]=1
#print(sub_ave_dic)
#print(x)
#print(count_dic)
max_dic = {}
min_dic={}
for score in score_list:
    if score[1] in max_dic:
        if score[2]>=max_dic[score[1]]:
            max_dic[score[1]]=score[2]
        elif score[2]<=min_dic[score[1]] :
            min_dic[score[1]]=score[2]
        else :pass
    else:
        max_dic[score[1]]=score[2]
        min_dic[score[1]]=score[2]
for key in sub_ave_dic.keys():
    sub_ave=sub_ave_dic[key]/count_dic[key]
    print('{0}の平均点は{1}点,最高点は{2}点,最低点は{3}点'.format(key,sub_ave,max_dic[key],min_dic[key]))
# 番号ごとの平均点
num_sum_dic={}
count_dic_2={}
for x in score_list:
    if x[0] in num_sum_dic:
        num_sum_dic[x[0]]+=x[2]
        count_dic_2[x[0]]+=1
    else :
        num_sum_dic[x[0]]=x[2]
        count_dic_2[x[0]]=1
for key,sum_score in num_sum_dic.items():
    num_ave=sum_score/count_dic_2[key]
    print('{0}番の平均点は{1}点です。'.format(key,num_ave))
