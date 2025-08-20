a = 123
# print(a[0])

b = '123'
print(b[0])
# b[0] = '4'
b = b + '4'
if '1' in b:
    print('yes')
b = b*2

c = ['1', [2, 4], 3]
print(c[1][1])
c[2] = 4
# c = c + 4
c = c + [4, 5]
if '1' in c:
    print('yes')


d = {1, 2, 3}
# print(d[0])
# d = d + {4}
d = d | {4}
if '1' in d:
    print('yes')

e = (1, 2, 3)
print(e[0])
# e[0] = 5
# e = e + (4)
if '1' in e:
    print('yes')
