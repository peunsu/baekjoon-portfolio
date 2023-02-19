import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([(0, 0, 0)])
while q:
    x, y, flag = q.popleft()

    if (x, y) == (n-1, m-1):
        print(visited[x][y][flag])
        break

    for i, j in zip(dx, dy):
        x_, y_ = x+i, y+j

        if not 0 <= x_ < n or not 0 <= y_ < m:
            continue

        if visited[x_][y_][flag]:
            continue

        if field[x_][y_] and not flag:
            q.append((x_, y_, 1))
            visited[x_][y_][1] = visited[x][y][flag] + 1
        if not field[x_][y_]:
            q.append((x_, y_, flag))
            visited[x_][y_][flag] = visited[x][y][flag] + 1
else:
    print(-1)