
T = int(input())

a = [[0] * 14 for i in range(15)]

for i in range(14):
    a[0][i] = i+ 1

for j in range(1, 15):
    for i in range(0, 14):
        if i == 0:
            a[j][i] = 1
        else:
            for x in range(i + 1):
                a[j][i] += a[j-1][x]

for i in range(T):
    k = int(input())
    n = int(input())
    print(a[k][n])