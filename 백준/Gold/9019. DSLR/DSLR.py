import sys
from collections import deque

input = sys.stdin.readline

def dslr(n: int, cmd: str) -> int:
    if cmd == 'D':
        n *= 2
        return n if n < 10000 else n % 10000
    if cmd == 'S':
        return n - 1 if n != 0 else 9999
    if cmd == 'L':
        return (n % 1000) * 10 + n // 1000
    if cmd == 'R':
        return n // 10 + (n % 10) * 1000


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    visited = [0] * 10000

    queue = deque([(a, '')])
    visited[a] = 1
    while queue:
        p, c = queue.popleft()
        if p == b:
            print(c)
            break
        for oper in ['D', 'S', 'L', 'R']:
            q = dslr(p, oper)
            if not visited[q]:
                visited[q] = 1
                queue.append((q, c+oper))