k=0
f = open('9(4).txt').readlines()
for s in f:
    b = s.split()
    b = sorted(list(map(int,b)))
    a = []
    c=[]
    z=[]
    for x in b:
        if b.count(x)==3:
            print(1)
            a.append(x)
        if x%2==0:
            c.append(x)
        else:
            z.append(x)
    if len(set(a))==1 and len(z)<len(c) and (b[4]+b[5])>(sum(b)-(b[4]+b[5]))*2:
        k+=1
print(k)