import sys
N = int(input())
for i in range(N):
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    count = 0
    index = 0
    while index <= M:
        if len(arr) == 1:
            count+=1
            break
        maxnum = max(arr)
        b = arr.pop(0)
        if maxnum == b:
            count += 1
            if index == M:
                break
        else:   
            arr.append(b)
            if index == M:
                M = len(arr) + M
        index+=1
    print(count)


# t = int(input())

# for _ in range(t):
#     n,m = map(int, input().split())
#     data = list(map(int, input().split()))

#     result = 1
#     while data:
#         if data[0] < max(data):
#             data.append(data.pop(0))
#         else:
#             if m == 0 : break

#             data.pop(0)
#             result += 1

#         if m > 0:
#             m = m -1
#         else:
#             m = len(data) -1
    
#     print(result)