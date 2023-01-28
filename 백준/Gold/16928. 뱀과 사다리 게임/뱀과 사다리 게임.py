import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0] * 101
visited = [0] * 101
result = [100] * 101

for _ in range(n+m):
    a, b = map(int, input().split())
    graph[a] = b

queue = deque([1])
result[1] = 0
while queue:
    v = queue.popleft()

    if v == 100:
        break

    for i in range(1, 7):
        u = v + i
        if u <= 100 and not visited[u]:
            if graph[u]:
                u = graph[u]
            
            queue.append(u)
            visited[u] = 1
            result[u] = min(result[u], result[v] + 1)

print(result[100])