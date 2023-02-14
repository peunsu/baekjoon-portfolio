import sys
input = sys.stdin.readline
INF = float('inf')

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

n = int(input())
m = int(input())

cost = [[0 if i == j else INF for j in range(n)] for i in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

floyd()

for cs in cost:
    for c in cs:
        if c >= INF:
            print(0, end=" ")
        else:
            print(c, end=" ")
    print()