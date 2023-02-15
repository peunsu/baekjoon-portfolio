import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100001
visited[n] = 0

cnt = 0

q = deque([n])
while q:
    v = q.popleft()

    if v == k:
        cnt += 1

    for v_ in [2*v, v-1, v+1]:
        if v_ < 0 or v_ > 100000:
            continue
        if visited[v_] == -1 or visited[v_] >= visited[v] + 1:
            visited[v_] = visited[v] + 1
            q.append(v_)

print(visited[k])
print(cnt)