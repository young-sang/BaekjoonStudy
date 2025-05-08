def res(arr):
    result = 0
    for i in arr:
        adder = int(i) * int(i)
        result += adder
    print(result % 10)

a = input().split(' ')
res(a)