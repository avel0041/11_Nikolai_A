f = open('17_3.txt').readlines()
res=[]
a = list(map(int,f))

def f(a):
    if a%10==6 and len(str(abs(a))) == 4:
        return 1
    return 0

for s in a:
    z = str(abs(s))
    if s>0 and s%10==6 and len(z)==4:
        res.append(s)

x = min(res)
res2=[]
for i in range(0,len(a)-2):
    if (a[i]+a[i+1]+a[i+2])<=x and (f(a[i]) + f(a[i+1]) + f(a[i+2]) == 1):
        res2.append(a[i]+a[i+1]+a[i+2])
print(len(a),max(res))