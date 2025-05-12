res = {}
while True:
    try:
        a, b, c = input().split()
        if b not in res:
            res[b] = 0

        if c == "right":
            res[b] *= -1
            res[b] += int(a)
        else:
            res[b] -= 20

    except:
        break
num = 0
res1 = 0
for k in res:
    if res[k]>0:
        num += 1
        res1 += res[k]

print(num, res1)