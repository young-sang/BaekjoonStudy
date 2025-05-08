N = int(input())
arr = []
for i in range(N):
    x, y = input().split()
    x = int(x)
    arr.append((x,y))

a = sorted(arr, key=lambda x: x[0])

for x, y in a:
    print(x, y)