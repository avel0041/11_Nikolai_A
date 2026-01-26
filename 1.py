f=open('241.txt').readline()
mx = 52
st = ''
for s in 'EIOU':
    f=f.replace(s,'*')
for l in range(len(f)-1):
    if f[l] != 'A':
        continue
    for r in range(l+mx, len(f)):
        if f[r] != 'Z':
            continue
        s = f[l:r+1]
        su = 0
        for el in s:
            if el in '123456789':
                su += int(el)
        if (s.count('*')+s.count('A'))==50 and su%7==0 and s.count('Z')==1:
            z=len(s)
            if z>mx:
                mx=z
                st=s
        else:
            break
print(mx)
print(st)