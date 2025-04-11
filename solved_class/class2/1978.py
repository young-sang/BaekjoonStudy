N = int(input())
a = list(map(int, input().split()))

count = 0
for i in a:
    if i == 1:
        continue
    a = False
    for j in range(2, i):
        if i % j == 0:
            a = True
            break
    if a == False:
        count += 1

print(count)