kodomo=int(input("13才未満の人数は？"))
hutuu=int(input("13〜64才の人数は？"))
nenpai=int(input("65才以上の人数は？"))
sum_price=kodomo*500+hutuu*1000+nenpai*700
sum_number=kodomo+hutuu+nenpai
#i=sum_price*0.8
#print(i)
if sum_number>=10:
    print("チケットの合計料金は"+str(sum_price*0.8)+"円です")
else:
    print("チケットの合計料金は"+str(sum_price)+"円です")
