N = int(input())
arr = list(input())

code = [
    ["A", "C", "A", "G"],
    ["C", "G", "T", "A"],
    ["A", "T", "C", "G"],
    ["G", "A", "G", "T"]
]
def a(a):
    if a == "A":
        return 0
    elif a == "G":
        return 1
    elif a == "C":
        return 2
    else:
        return 3

for i in range(N-1):
    c = code[a(arr[len(arr)-1])][a(arr[len(arr)-2])]
    arr.pop()
    arr[-1] = c

print(arr[0])