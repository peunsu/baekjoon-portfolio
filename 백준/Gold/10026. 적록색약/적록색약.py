import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x: int, y: int):
    visited[x][y] = 1
    cur = graph[x][y]
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x+dx < n and 0 <= y+dy < n and graph[x+dx][y+dy] == cur and not visited[x+dx][y+dy]:
            dfs(x+dx, y+dy)

def dfs_color(x: int, y: int):
    visited_color[x][y] = 1
    cur = color_dict[graph[x][y]]
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x+dx < n and 0 <= y+dy < n and color_dict[graph[x+dx][y+dy]] == cur and not visited_color[x+dx][y+dy]:
            dfs_color(x+dx, y+dy)

n = int(input())

graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
visited_color = [[0 for _ in range(n)] for _ in range(n)]
color_dict = {'R': 1, 'G': 1, 'B': -1}

cnt = [0, 0]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt[0] += 1
        if not visited_color[i][j]:
            dfs_color(i, j)
            cnt[1] += 1

print(cnt[0], cnt[1], sep=" ")