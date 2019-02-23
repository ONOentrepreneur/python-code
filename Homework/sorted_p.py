# 4. リストLを昇順(小さい順)にソートした結果を返す関数sorted(L)を定義してください
def sorted(L):
    v=-1
    M=[]
    for i in L:
        M.insert(v,i)
        v-=1
    return M
print(sorted([3,5,8,2,9]))
