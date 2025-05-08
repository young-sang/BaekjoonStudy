N, K = map(int, input().split())
arr = []

for i in range(N):
    a = int(input())
    if len(arr) == 0:
        arr.append(a)
        continue
    if a % arr[len(arr)-1] == 0:
        arr.append(a)
res = 0
rest = K
for j in range(N):
    a = arr[len(arr)-j-1]
    fin =  rest // a
    res += fin
    rest = rest % a

print(res)