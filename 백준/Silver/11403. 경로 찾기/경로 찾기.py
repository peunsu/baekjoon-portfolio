import sys

input = sys.stdin.readline

def dfs(p: int, visited: list):
    for q in range(n):
        if graph[p][q] and not visited[q]:
            visited[q] = 1
            dfs(q, visited)
    return visited

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(*dfs(i, [0] * n))