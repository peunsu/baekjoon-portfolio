import sys
from itertools import combinations

input = sys.stdin.readline

def dfs(x: int, y: int, cnt: int, sumn: int):
    global maxn

    sumn += grid[x][y]

    if cnt == 3:
        maxn = max(maxn, sumn)
        return

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x+dx < n and 0 <= y+dy < m and not visited[x+dx][y+dy]:
            visited[x+dx][y+dy] = 1
            dfs(x+dx, y+dy, cnt+1, sumn)
            visited[x+dx][y+dy] = 0

def t_shape(x: int, y: int):
    global maxn

    for shape in combinations([(1, 0), (-1, 0), (0, 1), (0, -1)], 3):
        sumn = grid[x][y]
        for dx, dy in shape:
            if 0 <= x+dx < n and 0 <= y+dy < m:
                sumn += grid[x+dx][y+dy]
        maxn = max(maxn, sumn)
    

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

maxn = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, 0)
        visited[i][j] = 0

        t_shape(i, j)

print(maxn)