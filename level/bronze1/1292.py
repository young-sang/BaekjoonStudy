arr = []
n = 1
while True:
    if len(arr) > 1000:
        break
    for i in range(n):
        arr.append(n)
    n += 1
a,b = map(int, input().split())
sum = 0
for i in range(a-1, b):
    sum += arr[i]

print(sum)