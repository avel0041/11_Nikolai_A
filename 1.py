k=0
res=[]
res1=[]
f = open('17.txt').readlines()
for s in f:
    if int(s)>99 and int(s)<1000 and int(s)%10==8:
        z1=int(s)**2
        res.append(z1)
z=min(res)
a = list(map(int,f))
for i in range(len(f)-2):
    if (99<a[i]<1000 or 99<a[i+1]<1000 or 99<a[i+2]<1000):
        u1 = 0
        u2 = 0
        u3 = 0
        if a[i]**2>z:
            u1 = 1
        if a[i+1]**2>z:
            u2 = 1
        if a[i+2]**2>z:
            u3 = 1
        if u1+u2+u3==2:
            res1.append(a[i]+a[i+1]+a[i+2])
print(len(res1),max(res1))