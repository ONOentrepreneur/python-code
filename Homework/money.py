money=int(input("合計金額"))
#0<=money<=1000
#result="500円硬貨は{0}枚、100円硬貨は{1}枚、50円硬貨は{2}枚、10円硬貨は{3}枚、5円効果は{4}枚、1円硬貨は{5}枚".format(gohyaku,hyaku,gozyuu,zyuu,go,iti)
# 引いていく 引けなくなったら違うのを引く
#money==500*gohyaku+100*hyaku+50*gozyuu+10*zyuu+5*go+1*iti
a=0
b=0
c=0
d=0
e=0
f=0

while money>=a*500:
    a+=1
gohyaku=a-1
#print(gohyaku)
money=money-gohyaku*500
while money>=100*b:
    b+=1
hyaku=b-1
money-=hyaku*100
while money>=50*c:
    c+=1
gozyuu=c-1
money-=50*gozyuu
while money>=10*d:
    d+=1
zyuu=d-1
money-=10*zyuu
while money>=5*e:
    e+=1
go=e-1
iti=money-5*go

result="500円硬貨は{0}枚、100円硬貨は{1}枚、50円硬貨は{2}枚、10円硬貨は{3}枚、5円効果は{4}枚、1円硬貨は{5}枚".format(gohyaku,hyaku,gozyuu,zyuu,go,iti)

print(result)
