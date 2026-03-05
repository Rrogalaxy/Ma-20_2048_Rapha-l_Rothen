
def pack4 (a,b,c,d):
    if c ==0 :
        c,d = d,0
    if b == 0 :
        b,c,d = c,d,0
    if a == 0 :
        a,b,c,d = b,c,d,0

    if a == b :
        a,b,c,d = a*2,c,d,0
    if b == c :
        b,c,d = b*2,d,0
    if c == d :
        c,d = c*2,0

    return (a,b,c,d)

#print(pack4(0,0,0,2))
#print(pack4(0,0,2,2))
#print(pack4(2,0,2,2))
#print(pack4(2,2,2,2))
#print(pack4(2,2,4,0))

################################################