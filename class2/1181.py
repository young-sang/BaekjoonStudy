# N = int(input())

# arr = {}
# for i in range(N):
#     a = input()
#     letLen = str(len(a))
    
#     if letLen not in arr :
#         arr[letLen] = []
#     if a in arr[letLen]:
#         continue
#     arr[letLen].append(a)

# dic1 = dict(sorted(arr.items()))

# for j in dic1.keys():
#     a = sorted(dic1[j])
#     for z in a:
#         print(z)


# ------------------

N = int(input())

arr = []
for i in range(N):
    a = input()
    if a in arr:
        continue
    arr.append(a)


a = sorted(arr, key = lambda x : (len(x), x) )
for j in a:
    print(j)

