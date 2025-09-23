alphabet = sorted(set('0123456789QWERTYUIOPASDFGHJKLZXCVBNM'))
for p in range(8,36):
    for x in alphabet[0:p]:
        for y in alphabet[0:p]:
            if int('45', p) * int('67', p)==int(x + y + '2', p):
                print(int(y+x, p))
                break