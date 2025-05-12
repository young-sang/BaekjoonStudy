N = int(input())
res = []
arr = list(map(int, input().split()))
for i in range(1, len(arr) + 1):
    res.insert(arr[i-1],i)
    
print(' '.join(map(str, res[::-1])))