import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a: int, b: int):
    global cnt_cheese

    q = deque([(a, b)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if not 0 <= x_ < n and not 0 <= y_ < m:
                continue
                
            if paper[x_][y_]:
                visited[x_][y_] += 1
                continue

            if not visited[x_][y_]:
                visited[x_][y_] = 1
                q.append((x_, y_))
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                paper[i][j] = 0
                cnt_cheese -= 1

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

cnt_cheese = 0
for i in range(n):
    for j in range(m):
        if paper[i][j]:
            cnt_cheese += 1

time = 0
while cnt_cheese:
    visited = [[0] * (m) for _ in range(n)]
    visited[0][0] = 1
    bfs(0, 0)
    time += 1

print(time)