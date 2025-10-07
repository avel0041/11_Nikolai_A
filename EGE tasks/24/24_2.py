# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.
f=open('24_2.txt').readline()
# k=0
# k_max=0
# for i in range(0,len(f)-1):
#     if not((f[i]=='K' and f[i+1]=='L') or (f[i]=='L' and f[i+1]=='K')):
#         k+=1
#     else:
#         k_max=max(k,k_max)
#         k=0
# k_max=max(k,k_max)
# print(k_max+1)

f = f.replace('KL', 'K L')
f = f.replace('LK', 'L K')
f = f.split()

k_max=0
for el in f:
    if len(el)>k_max:
        k_max=len(el)

# k_max = max(f, key=len)

print(k_max)