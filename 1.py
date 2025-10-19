f={}
g={}
for n in range(0,130,-1):
    if n<3:
        g[n], f[n] = 1, 1
    if n>2 and n%2==0:
        f[n] = g[n]+f[n-1]
    if n > 2 and n%2!=0:
        f[n] = f[n-2] - g[n + 1]
    if n>2 and n%2==0:
        g[n] = f[n-3]+f[n-2]
    if n > 2 and n%2!=0:
        g[n] = f[n+1] -g[n-1]
print(g[120])