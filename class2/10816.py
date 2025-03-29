# import sys
# N = int(input())
# a = sorted(map(int, sys.stdin.readline().split(" ")))
# M = int(input())
# value = map(int, sys.stdin.readline().split(" "))


# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return array.pop(mid)
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     else:
#         return


# for i in b:
#     count = 0
#     while binary_search(a,i,0, len(a)-1):
#         count +=1
#     print(count, end=' ')

        
#     # ---

import sys
N = int(input())
a = sorted(map(int, sys.stdin.readline().split(" ")))
M = int(input())
value = map(int, sys.stdin.readline().split(" "))

count = {}
for card in a:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return count.get(target)
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    else:
        return 0


for target in value:
    print(binary_search(a, target, 0, len(a) -1), end=" ")

        
    