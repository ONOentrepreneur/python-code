def sosuu(v):

    i=2
    while i<=v:
        is_sosuu=True

        for k in range(2,i):
            if (i%k)==0:
                is_sosuu=False
                break
        if is_sosuu: yield i
        i+=1
it=sosuu(50)
print(it)
for n in it:
    print(n)
