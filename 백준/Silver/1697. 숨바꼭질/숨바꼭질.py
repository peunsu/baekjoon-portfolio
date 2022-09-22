from collections import deque

n, k = map(int, input().split())

pos = [-1] * 100001
pos[n] = 0

target = deque([n])
while target:
    x = target.popleft()
    for i in (2*x, x-1, x+1):
        if i < 0 or i > 100000:
            continue
        if pos[i] == -1:
            pos[i] = pos[x] + 1
            target.append(i)

print(pos[k])