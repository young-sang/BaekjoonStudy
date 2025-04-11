N = int(input())

arr = []

for i in range(N):
    a = int(input())
    arr.append(a) 
dp = [0] * (max(arr)+1)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5, max(arr)+1):
    dp[i] = dp[i-1] + dp[i-5]

for i in arr:
    print(dp[i])
