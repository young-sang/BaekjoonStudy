N, M = list(map(int, input().split(' ')))

a = list(map(int, input().split(' ')))

maxnum = 0

for i in a:
    b = a.copy()
    b.remove(i)
    for j in b:
        c = b.copy()
        c.remove(j)
        for x in c:
            res = i + j + x
            if(res <= M):
                if(res > maxnum):
                    maxnum = res

print(maxnum)