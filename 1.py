def f(x):
    res=[]
    n=2
    while n*n<=x:
        if x%n==0:
            x//=n
            res.append(n)
        else:
            n+=1
    if x>1:
        res.append(int(x))
    if len(res)==1:
        return 0
    return max(res)-min(res)
k=0
for i in range(3300000, 100000000000000000000000):
    if f(i)%10==5:
        if str(f(i))==str(f(i))[::-1]:
            print(i, f(i))
            k+=1
            if k==5:
                break

