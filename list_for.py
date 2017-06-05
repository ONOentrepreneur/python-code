# あるクラスの国語のテストの平均点
points=[88,76,67,43,79,80,91]
# テストの合計を求める
sum_v=0
for i in points:
    sum_v+=i
    print(str(i)+"点をを足して合計は"+str(sum_v)+"点")
# 平均を求める
av=sum_v/len(points)
print("平均点は"+str(av)+"点")
