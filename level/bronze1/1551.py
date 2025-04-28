N, K = map(int, input().split())
arr = list(map(int, input().split(",")))
res = arr
for i in range(K):
    for j in range(len(res)-1):
        res[j] = res[j+1] - res[j]
    res.pop()
print(",".join(map(str,res)))