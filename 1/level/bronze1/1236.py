a,b = map(int, input().split())
arr = []
for i in range(a):
    c = input()
    arr.append(c)
res_row = [False] * a
res_col = [False] * b
for i in range(a):
    for j in range(b):
        if arr[i][j] == "X":
            res_row[i] = "True"
            res_col[j] = "True"
x = 0
y = 0
for i in res_row:
    if i == False:
        x += 1
for i in res_col:
    if i == False:
        y += 1

if x >= y:
    print(x)
else:
    print(y)