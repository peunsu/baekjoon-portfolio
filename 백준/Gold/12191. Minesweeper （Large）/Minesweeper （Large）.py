import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    mine = [list(input().rstrip()) for _ in range(n)]
    
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if mine[i][j] == "*":
                for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n and mine[nx][ny] == ".":
                        mine[nx][ny] = "+"
    
    for i in range(n):
        for j in range(n):
            if mine[i][j] == ".":
                cnt += 1
                q = deque([(i, j)])
                mine[i][j] = "-"
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if mine[nx][ny] == ".":
                                q.append((nx, ny))
                                mine[nx][ny] = "-"
                            elif mine[nx][ny] == "+":
                                mine[nx][ny] = "-"
                            
    
    for i in range(n):
        for j in range(n):
            if mine[i][j] == "+":
                cnt += 1
    
    return cnt

t = int(input())
for i in range(t):
    print(f"Case #{i+1}: {solve()}")