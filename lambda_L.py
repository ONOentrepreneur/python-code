# L = [ ['田中', '山下', '中村', '村上', '江口'], [35, 69, 21, 12, 46]]
def sorted(L):
    younger_L=sorted(L,
    key=lambda  x:x[1],
    reverse=False)
    return younger_L
print(sorted([ ['田中', '山下', '中村', '村上', '江口'], [35, 69, 21, 12, 46]]))
