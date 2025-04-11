# import sys

# def fibonacci(n, dic):
#     if n == 0:
#         dic["0"] += 1
#         return 0
#     elif n == 1:
#         dic["1"] += 1
#         return 1
#     else:
#         return fibonacci(n-1, dic) + fibonacci(n-2, dic)

# N = int(sys.stdin.readline())
# for i in range(N):
#     dic = {
#         "0": 0,
#         "1": 0
#     }
#     a = sys.stdin.readline()
#     fibonacci(int(a), dic)
#     print(dic["0"], end=" ")
#     print(dic["1"])

# ---------------------------

N = int(input())
for i in range(N):
    T = int(input())
    a,b = 1, 0
    for j in range(T):
        a,b = b, a+b
    print(a,b)
