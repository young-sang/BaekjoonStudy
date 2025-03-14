a = int(input())

for i in range(0, a):
    b = input()
    res = 0
    count = 1
    for j in b:
        if j == "O":
            res += count
            count += 1
        else:
            count = 1
    print(res)
