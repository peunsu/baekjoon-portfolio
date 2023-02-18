import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if graph[i][j] <= m:
            temp += items[j]
    result = max(result, temp)

print(result)