import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    a = int(sys.stdin.readline())
    arr.append(a)

arr.sort()

maxnum = max(arr)
minnum = min(arr)

print(round(sum(arr) / N))
print(arr[N // 2])

count =  [0] * (maxnum - minnum+1)
for i in arr:
    if minnum < 0:
        count[i-minnum] += 1
    else:
        count[i-minnum] += 1

maxCount = max(count)
m = 0
countarr = []
for c in range(len(count)):
    if count[c] == maxCount:
        countarr.append(c+minnum)

if len(countarr) > 1:
    print(countarr[1])
else:
    print(countarr[0])


print(arr[-1] - arr[0])


# dic = dict()
# for i in arr:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# mx = max(dic.values())
# mx_dic = []
# for i in dic:
#     if mx == dic[i]:
#         mx_dic.append(i)
# if len(mx_dic) > 1:
#     print(mx_dic[1])
# else:
#     print(mx_dic[0])