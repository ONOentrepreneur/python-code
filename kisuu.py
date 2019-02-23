def gen():
    i=1
    while i<=30:
        yield i
        i+=2
it= gen()
for v in it:
    print(v,end=",")
