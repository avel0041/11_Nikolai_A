# Текстовый файл состоит не более чем из 10^6 символов A, B и C. 
# Определите максимальное количество идущих подряд символов C.
f = open('24_0.txt').readline()

k = 0
res=[]
k_max=0
for s in f:
    if s=='C':
        k+=1
    else:
        if k > k_max:
            k_max = k
        k=0
if k > k_max:
    k_max = k
print(k_max)
