N = int(input())
T = int(input())

graph = {i+1 : [] for i in range(N)}
visited = [False] * (N+1)

for i in range(T):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n, count):
    visited[n] = True
    if n != 1:
        count +=1 
    for i in graph[n]:
        if not visited[i]:
            count = dfs(i, count)
    return count

a = dfs(1, 0)

print(a)
