import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
in_degree[0] = -1

for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1):
        a, b = temp[i], temp[i+1]
        graph[a].append(b)
        in_degree[b] += 1

def topological_sort():
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    result = []
    for i in range(n):
        if not q:
            break
        v = q.popleft()
        result.append(str(v))
        for v_ in graph[v]:
            in_degree[v_] -= 1
            if in_degree[v_] == 0:
                q.append(v_)
    else:
        return result

    return ["0"]

print("\n".join(topological_sort()))