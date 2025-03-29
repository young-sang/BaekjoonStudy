import sys
stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    return 0

def top():
    if len(stack) == 0:
        return -1
    return stack[len(stack) - 1]

N = int(input())

for i in range(N):
    a = sys.stdin.readline().strip()
    if "push" in a:
        b = a.split(' ')
        push(b[1])
    elif "pop" in a:
        print(pop())
    elif "size" in a:
        print(size())
    elif "empty" in a:
        print(empty())
    elif "top" in a:
        print(top())