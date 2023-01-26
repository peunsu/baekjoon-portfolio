import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = []
queue = deque()

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                queue.append((i, j, k))
    graph.append(temp)



while queue:
    l = len(queue)
    for _ in range(l):
        x, y, z = queue.popleft()
        for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1),
                        (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
            if 0 <= x + dx < h and 0 <= y + dy < n and 0 <= z + dz < m and graph[x+dx][y+dy][z+dz] == 0:
                queue.append((x+dx, y+dy, z+dz))
                graph[x+dx][y+dy][z+dz] = graph[x][y][z] + 1

cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(graph[i][j]))

print(cnt-1)