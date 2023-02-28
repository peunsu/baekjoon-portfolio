import sys
from collections import deque
input = sys.stdin.readline

def topological_sort():
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    result = time.copy()
    while q:
        v = q.popleft()
        for v_ in graph[v]:
            in_degree[v_] -= 1
            result[v_] = max(result[v_], result[v] + time[v_])
            if in_degree[v_] == 0:
                q.append(v_)
    
    return result

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    in_degree[0] = -1

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    acm_time = topological_sort()
    w = int(input())
    print(acm_time[w])