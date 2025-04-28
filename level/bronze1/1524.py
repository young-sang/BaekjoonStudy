N = int(input())

for i in range(N):
    input()
    a, b = map(int, input().split())
    arr_s = sorted(list(map(int, input().split())), reverse=True)
    arr_b = sorted(list(map(int, input().split())), reverse=True)

    while arr_s and arr_b:
        if arr_s[-1] >= arr_b[-1]:
            arr_b.pop()
        else:
            arr_s.pop()
    if arr_s:
        print('S')
    elif arr_b:
        print('B')
    else:
        print('C')