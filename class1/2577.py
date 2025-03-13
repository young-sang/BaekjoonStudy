A = int(input())
B = int(input())
C = int(input())

a = A * B * C
a = str(a)

b = [0,0,0,0,0,0,0,0,0,0]
for i in a:
    i = int(i)
    b[i] = b[i] + 1

for i in b:
    print(i)