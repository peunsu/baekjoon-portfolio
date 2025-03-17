import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, visited, keys):
    global cnt
    
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        i, j = queue.popleft()
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = i + dx, j + dy
            
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    
                    if floor[nx][ny] == '*':
                        continue
                    if floor[nx][ny] == '.':
                        queue.append((nx, ny))
                    elif floor[nx][ny] == '$':
                        cnt += 1
                        queue.append((nx, ny))
                        floor[nx][ny] = '.'
                    elif 'a' <= floor[nx][ny] <= 'z':
                        keys.add(floor[nx][ny])
                        floor[nx][ny] = '.'
                        visited = [[False] * (w + 2) for _ in range(h + 2)]
                        queue.clear()
                        queue.append((nx, ny))
                    elif 'A' <= floor[nx][ny] <= 'Z':
                        if floor[nx][ny].lower() in keys:
                            queue.append((nx, ny))
                            floor[nx][ny] = '.'
                    
        

n = int(input())

answer = []

for _ in range(n):
    h, w = map(int, input().split())
    floor = [['.'] + list(input().rstrip()) + ['.'] for _ in range(h)]
    floor = [['.'] * (w + 2)] + floor + [['.'] * (w + 2)]
    keys = set(list(input().rstrip()))
    
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    cnt = 0
    
    bfs(0, 0, visited, keys)
    
    answer.append(cnt)

for a in answer:
    print(a)