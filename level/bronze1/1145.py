arr = list(map(int, input().split()))
num = 0
while True:
    num += 1
    count = 0
    for i in arr:
        if num % i == 0:
            count += 1
    if count >= 3:
        print(num)
        break