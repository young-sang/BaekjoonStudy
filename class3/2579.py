N = int(input())
dp = [0] * (N)
s = [int(input()) for _ in range(N)]

if len(s) <= 2:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0]+s[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3]+ s[i-1] + s[i], dp[i-2]+ s[i])
    print(dp[-1])