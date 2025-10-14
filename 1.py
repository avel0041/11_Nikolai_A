def f(s, e, v):
    if s>e:
        return 0
    if s==e:
        return 1
    if ('11' in v) or ('22' in v):
        return 0
    return f(s+1, e, v+'1') + f(s+2, e, v+'1') + f(s*2,e,v+'2') + f(s*3, e,v+'2') 

print(f(1, 24, ''))
