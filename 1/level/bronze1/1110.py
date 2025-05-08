a = int(input())
num = 0
res = a
while True:
    num += 1
    tems = res // 10
    ones = res % 10
    sum = tems + ones
    res = ones * 10 + (sum % 10)

    if res == a:
        print(num)
        break