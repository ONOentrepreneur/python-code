

try:
    print('じゃんけんしましょう')
    import random
    user=input("どの手を出しますか")
    hand={"グー":0,"チョキ":1,"パー":2}
    cp=random.randint(0,2)
    j=(hand[user]-cp+3)%3

    if j==0:
        print("あいこ")
    elif j==1:
        print("負け")
    elif j==2:
        print("勝ち")
except :
    print("もう一度入力してください")
