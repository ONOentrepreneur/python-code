#2. リストLと二つの数l,rが与えられて、Lのl番目からr番目までの要素の合計を返す関数cumsum(L, l, r)を定義してください

def cumsum(L,l,r):
    sum=0
    for i in range(l,r):
        sum+=L[i]
    return sum

print(cumsum([1,2,5,6],2,4))
