import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(input().rstrip()) for _ in range(n)]
dist = [[0] * (m) for _ in range(n)]

q = deque([(0, 0)])
dist[0][0] = 1
while q:
    x, y = q.popleft()
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if 0 <= x+dx < n and 0 <= y+dy < m and maze[x+dx][y+dy] == "1" and not dist[x+dx][y+dy]:
            dist[x+dx][y+dy] = dist[x][y] + 1
            q.append((x+dx, y+dy))

print(dist[n-1][m-1])