animals={"チーター":110,"トナカイ":80,"シマウマ":60,"ライオン":58,"キリン":50,"ラクダ":30}
location={"静岡":182.7,"名古屋":350.6,"大阪":507.5}
def calctime(animal,speed,ken,leng):
    print("{0}は{1}まで{2}時間".format(animal,ken,round(leng/speed,1)))
for a,s in animals.items():
    for k,l in location.items():
        calctime(a,s,k,l)
