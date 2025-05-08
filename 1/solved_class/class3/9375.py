N = int(input())
for i in range(N):
    a = int(input())
    case = {}
    for j in range(a):
        x, y = input().split()
        if y not in case.keys():
            case[y] = []
        case[y].append(x)
    res = 1
    for i in case.values():
        res *= (len(i)+1)
    res -= 1
    print(res)