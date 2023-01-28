import sys
from collections import deque

input = sys.stdin.readline

def bfs(p: int, q: int) -> list:
    visited = [[0] * n for _ in range(n)]

    queue = deque([(p, q)])
    visited[p][q] = 1

    temp = []

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx = x + dx; ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and space[nx][ny] <= size:
                if 0 < space[nx][ny] < size:
                    temp.append((nx, ny, visited[x][y]))
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    temp.sort(key=lambda x: (x[2], x[0], x[1]))

    return temp


n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            start = (i, j)
            space[i][j] = 0
            break

size = 2
cnt = 0
time = 0

while True:
    cur = bfs(*start)

    if len(cur) == 0:
        break
    
    nx, ny, time_ = cur.pop(0)

    space[nx][ny] = 0
    cnt += 1
    time += time_
    if cnt == size:
        size += 1
        cnt = 0
    
    start = (nx, ny)

print(time)