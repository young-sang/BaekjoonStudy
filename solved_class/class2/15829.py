alpha = 'abcdefghijklmnopqrstuvwxyz'

a = int(input())

M = 1234567891

b = input()
res = 0

for i in range(0, len(b)):
        res += ((alpha.index(b[i]) + 1) * (31 ** i))
        

print(res % M)