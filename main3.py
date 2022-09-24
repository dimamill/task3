x = int(input('X: '))
rim = ''
S1 = {1: 'IVX', 10: 'XLC', 100: 'CDM', 1000: 'M  '}
 
for i in (1000, 100, 10, 1):
    if x // i != 0:
        a, b, c = S1[i]
        S = (a, a * 2, a * 3, a + b, b, b + a, b + 2 * a, b + 3 * a, a + c)
        rim += S[x // i - 1]
        x = x- (x// i) * i
print(rim)
