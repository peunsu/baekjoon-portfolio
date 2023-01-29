import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v: int):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

n = int(input())

graph = [list() for _ in range(n+1)]
visited = [0] * (n+1)
visited[1] = -1

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for v in visited[2:]:
    print(v)