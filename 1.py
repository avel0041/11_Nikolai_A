from itertools import*
k=0
a = product('АБВГД', repeat = 5)
for n in a:
    v = ''.join(n)
    if v[0]!='А' and 'АА' not in v and 'ББ' not in v and 'ВВ' not in v and 'ГГ' not in v and 'ДД' not in v:
        k+=1
print(k)

def f(x):
    for i in range(len(x)):
        if x[i] != x[i+1]:


