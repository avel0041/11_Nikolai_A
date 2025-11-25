from re import*
f = 'ABCBCBABFJSKLAJKFLABCBS:LADJJ'
r = r'[1-9A-D][0-9A-D]*[02468AC]'
v = findall(r, f)
b = max(v, key=len)
print(len(b))
