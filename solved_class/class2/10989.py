import sys

N = int(sys.stdin.readline())
cnt = [0] * (10000 + 1)

for i in range(N):
    cnt[int(sys.stdin.readline())] += 1

for i in range(len(cnt)):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)

# 계수정렬에 대해서