"""
3.
>>> L = [ ['田中', 35] ['山下', 69], ['中村', 21], ['村上', 12], ['江口', 46] ]
>>> sorted(L)
[ ['村上', 12], ['中村', 21], ['田中', 35], ['江口', 46], ['山下', 69] ]
```

となるような２次元配列の並び替えを行う関数sortedを実装してください
Lは
```
[ ['村上', 12],
  ['中村', 21],
  ['田中', 35],
  ['江口', 46],
  ['山下', 69] ]
"""
def sorted(L):
    dic={}
    n=0
    for i in range(0,len(L)):
        dic[L[n][1]]=L[n][0]
        n+=1
    age=[]
    for i in range(0,len(L)):
        age.append(L[i][1])
    for i in range(1,len(age)):
        j = i
        while (j > 0) and (age[j-1] > age[j]) :
            tmp = age[j-1]
            age[j-1] = age[j]
            age[j] = tmp
            j -= 1
    n=0
    for i in range(0,len(age)):
        L[n][1]=age[n]
        n+=1

    n=0
    for i in age:
        L[n][0]=dic[i]
        n+=1
    return L

print(sorted([ ['田中', 35] ,['山下', 69], ['中村', 21], ['村上', 12], ['江口', 46] ]))
