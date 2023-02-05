import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
_, *truth = map(int, input().split())

visited = [0] * (m)

party = [list(map(int, input().split()))[1:] for _ in range(m)]

queue = deque(truth)
while queue:
    people = queue.popleft()
    for i in range(m):
        if visited[i]:
            continue
        if people in party[i]:
            visited[i] = 1
            queue.extend(party[i])

print(visited.count(0))