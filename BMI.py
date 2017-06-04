weight=float(input("体重（kg）は？"))
height=float(input("身長（cm）は？"))
height_m=height/100
bmi=weight/(height_m**2)
result=""
if bmi<18.25:
    result="痩せ型"
if 18.5<=bmi<25:
    result="普通体重"
if 25<=bmi<30:
    result="肥満（軽）"
if bmi>=30:
    result="肥満（重）"
print("BMI：",bmi)
print("判定：",result)
