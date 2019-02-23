#3. `1,1,2,3,5,8,13,21`と一つ前と二つ前の数値を足した数からなる数列をフィボナッチ数列と言います。n番目のフィボナッチ数列の要素を返す関数fib(n)を定義してください
n=int(input("nは？"))
def fib(n):
    if n<=2:return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(n))
