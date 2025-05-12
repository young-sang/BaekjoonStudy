N = int(input())

for i in range(N):
    arr = input().split(' ')
    res = []
    for j in range(len(arr)):
        res.append(arr.pop())
    print("Case #"+ str(i+1) + ": " + ' '.join(res))