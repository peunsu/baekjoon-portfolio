import sys
from collections import deque
input = sys.stdin.readline

def half(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return 0

def remove_one(n: int) -> int:
    if n % 10 == 1:
        return n // 10
    return 0

def bfs(b: int) -> int:
    queue = deque([(b, 1)])

    while queue:    
        v, cnt = queue.popleft()
        for func in [half, remove_one]:
            n = func(v)
            if n != 0:
                if n == a:
                    return cnt + 1
                queue.append((n, cnt+1))
    return -1

a, b = map(int, input().split())

print(bfs(b))