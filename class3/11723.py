import sys
arr = [0 for i in range(1, 21)]
N = int(sys.stdin.readline())

for i in range(N):
    text = sys.stdin.readline().split()

    if "add" in text:
        num = int(text[-1])
        arr[num-1] = num
    elif "remove" in text:
        num = int(text[-1])
        arr[num-1] = 0
    elif "check" in text:
        num = int(text[-1])
        if arr[num-1] == num:
            print(1)
        else:
            print(0)
    elif "toggle" in text:
        num = int(text[-1])
        if arr[num-1] == 0:
            arr[num-1] = num
        else:
            arr[num-1] = 0
    elif "all" in text:
        arr = [i for i in range(1, 21)]
    elif "empty" in text:
        arr = [0 for i in range(1,21)]