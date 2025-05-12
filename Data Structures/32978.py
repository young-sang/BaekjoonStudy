N = int(input())

arr = input().split()
res_arr = input().split()

for i in res_arr:
    arr.remove(i)

print(arr[0])