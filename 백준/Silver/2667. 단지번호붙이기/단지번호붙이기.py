import sys

input = sys.stdin.readline

def dfs(x: int, y: int):
    global cnt
    visited[x][y] = 1
    cnt += 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x+dx < n and 0 <= y+dy < n and graph[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
            dfs(x+dx, y+dy)

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

num = []
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            num.append(cnt)
            cnt = 0

num.sort()

print(len(num))
for n in num:
    print(n)