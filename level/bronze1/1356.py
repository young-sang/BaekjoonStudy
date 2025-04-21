a = input()
res = "NO"
for i in range(1, len(a)):
    x = list(a[:i])
    y = list(a[i:])
    x_res = 1
    y_res = 1
    for i in x:
        x_res *= int(i)

    for i in y:
        y_res *= int(i)

    if x_res == y_res:
        res = "YES"
        break

print(res)