# 国語の点数
points=[80,40,23,14,29,58,]
# 30点未満だけ赤点
akaten=[]
for p in points:
    if p<30:
        akaten.append(p)
print(akaten)
