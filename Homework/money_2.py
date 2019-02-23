money=int(input("合計金額"))
#0<=money<=1000
#result="500円硬貨は{0}枚、100円硬貨は{1}枚、50円硬貨は{2}枚、10円硬貨は{3}枚、5円効果は{4}枚、1円硬貨は{5}枚".format(gohyaku,hyaku,gozyuu,zyuu,go,iti)
# 引いていく 引けなくなったら違うのを引く
#money==500*gohyaku+100*hyaku+50*gozyuu+10*zyuu+5*go+1*iti
if money>=500:
        gohyaku=money//500
        hyaku=(money%500)//100
        gozyuu=((money%500)%100)//50
        zyuu=(((money%500)%100)%50)//10
        go=((((money%500)%100)%50)%10)//5
        iti=((((money%500)%100)%50)%10)%5

elif money>=100:

        hyaku= money//100
        gozyuu=(money%100)//50
        zyuu=((money%100)%50)//10
        go=(((money%100)%50)%10)//5
        iti=(((money%100)%50)%10)%5

elif money>=50:
        gozyuu=money//50
        zyuu=(money%50)//10
        go=((money%50)%10)//5
        iti=((money%50)%10)%5

elif money>=10:
        zyuu=money//10
        go=(money%10)//5
        iti=(money%10)%5

elif money>=5:
        go=money//5
        iti=money%5
elif money>=0:
        iti=money
result="500円硬貨は{0}枚、100円硬貨は{1}枚、50円硬貨は{2}枚、10円硬貨は{3}枚、5円効果は{4}枚、1円硬貨は{5}枚".format(gohyaku,hyaku,gozyuu,zyuu,go,iti)

print(result)
