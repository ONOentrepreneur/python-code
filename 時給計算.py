user=input("時給はいくらですか？")
jikyuu=int(user)
user=input("何時間働きましたか？")
jikan=int(user)
kyuuryou=jikyuu*jikan
fmt="時給{0}円で、{1}時間働いたので給料は、{2}円です。"
desc=fmt.format(jikyuu,jikan,kyuuryou)
print(desc)
