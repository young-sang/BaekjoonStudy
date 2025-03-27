import sys
from collections import deque
N = int(sys.stdin.readline())
deque = deque(range(1, N+1))

while len(deque) > 1:
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)

print(deque[0])

# ---

# N = int(sys.stdin.readline())
# arr = list(range(1, N+1))

# while len(arr) > 1:
#     arr.pop(0)
#     temp = arr.pop()
#     arr.append(temp)

