from collections import deque
from itertools import chain
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

tomatos = [[0] * m for _ in range(n)]
queue = deque()

for j in range(n):
    temp = map(int, input().split())
    for i, t in enumerate(temp):
        tomatos[j][i] = t
        if t == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i, j in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        if i < 0 or i >= m or j < 0 or j >= n:
            continue
        if tomatos[j][i] or tomatos[j][i] == -1:
            continue
        tomatos[j][i] = tomatos[y][x] + 1
        queue.append((i, j))

result = list(chain(*tomatos))
if 0 in result:
    print(-1)
else:
    print(max(result)-1)