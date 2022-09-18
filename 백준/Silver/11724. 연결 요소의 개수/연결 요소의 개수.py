import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(d: int):
    result[d] = 1
    for i in range(1, n+1):
        if (result[i]) or (net[d][i] == 0):
            continue
        dfs(i)
        

n, m = map(int, input().split())

net = [[0] * (n+1) for _ in range(n+1)]
result = [0] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    net[a][b] = 1
    net[b][a] = 1

for i in range(1, n+1):
    if not result[i]:
        dfs(i)
        cnt += 1

print(cnt)