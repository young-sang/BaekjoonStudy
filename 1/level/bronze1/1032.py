N = int(input())
arr = []
for i in range(N):
    a = input()
    arr.append(a)
if len(arr) == 1:
    print(arr[0])
else:
    res = list(arr[0])
    for j in range(1, len(arr)):
        for i in range(len(res)):
                if res[i] != arr[j][i]:
                    res[i] = '?'
                    
                    

    print(''.join(res))