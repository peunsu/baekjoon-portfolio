import sys
from collections import deque

input = sys.stdin.readline

def bacon(s: int) -> int:
    bacon = [0] * (n+1)
    visited = [0] * (n+1)
    
    q = deque([s])
    visited[s] = 1

    while q:
        i = q.popleft()
        for j in range(1, n+1):
            if graph[i][j] == 1 and not visited[j]:
                q.append(j)
                visited[j] = 1
                bacon[j] = bacon[i] + 1
    
    return sum(bacon)
        

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1

minv = 1000000
for i in range(1, n+1):
    v = bacon(i)
    if minv > v:
        minv = v
        minp = i

print(minp)