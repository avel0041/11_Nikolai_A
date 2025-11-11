def delitel(n):
    res=[]
    for x in range(1,int(n**0.5)+1):
        if n%x==0:
            res.append(x)
            res.append(n//x)
    return set(res)

def delitel1(n):
    res=[]
    x=1
    while x**2<=n:
        if n%x==0:
            res.append(x)
            res.append(n//x)
        x+=1
    return set(res)
    
def prost_del(n):
    res=[]
    x = 2
    while x*x<=n:
        while n%x==0:
            res.append(x)
            n = n//x
        x+=1
    if n > 1:
        res.append(int(n))
    return res


# x = 600_000
# q = []
# a = []
# c = 0
# while c < 5:
#     for i in range(17, int(x**0.5) + 1, 10):
#         if x%i==0:
#             q.append(x)
#             a.append(i)
#             c+=1
#             break
#     x += 1
# print(q, a)

res = []
for n in range(2_000_000,3_000_001):
    c=0
    for i in range(1000,int(n**0.5)+1):
        if n%i==0:
            if n//i-i<=115:
                c+=1
                if c>=3:
                    res.append(int(n))
                    break
print(res)

