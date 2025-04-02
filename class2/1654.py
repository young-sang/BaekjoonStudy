K, N = map(int, input().split())
arr = []
for i in range(K):
    a = int(input())
    arr.append(a)


def binarySearch(max, target):
    left = 1
    right = max

    while left <= right:
        mid = (left + right) // 2
        res = 0
        for i in arr:
            res += (i // mid)

        if res < target:
            right = mid - 1
        else:
            left = mid + 1
    return right

print(binarySearch(max(arr), N))

# # ---
# K, N = map(int, input().split())
# arr = []
# for i in range(K):
#     a = int(input())
#     arr.append(a)


# left = 1
# right = max(arr)

# while left <= right:
#     mid = (left + right) // 2
#     res = 0
#     for i in arr:
#         res += (i // mid)

#     if res < N:
#         right = mid - 1
#     else:
#         left = mid + 1

# print(right)