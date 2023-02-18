import sys
from itertools import combinations

input = sys.stdin.readline

def dfs(x: int, y: int):
    visited[x][y] = 1
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= x+dx < n and 0 <= y+dy < m and graph[x+dx][y+dy] == 0 and visited[x+dx][y+dy] == 0:
            dfs(x+dx, y+dy)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
wall = []
virus = []
size = n * m

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall.append((i, j))
        elif graph[i][j] == 1:
            size -= 1
        elif graph[i][j] == 2:
            virus.append((i, j))

min_cnt = 100

for combi in combinations(wall, 3):
    for i, j in combi:
        graph[i][j] = 1

    for i, j in virus:
        dfs(i, j)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                cnt += 1
        
    for i, j in combi:
        graph[i][j] = 0
    
    min_cnt = min(min_cnt, cnt)
    visited = [[0] * m for _ in range(n)]

print(size - min_cnt - 3)