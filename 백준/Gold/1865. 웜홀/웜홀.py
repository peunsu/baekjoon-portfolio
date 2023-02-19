import sys
input = sys.stdin.readline

INF = 1e9

def bellman(start: int):
    cost = [INF] * (n+1)
    cost[start] = 0

    for i in range(n):
        for s, e, t in edges:
            if cost[e] > cost[s] + t:
                if i == n-1:
                    return "YES"
                cost[e] = cost[s] + t
    return "NO"

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    print(bellman(1))