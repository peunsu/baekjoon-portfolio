import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
dp = [float('inf')] * (n+1)
dp[n] = 0
prev = [0] * (n+1)

heap = []
heappush(heap, (0, n))
while heap:
    c, v = heappop(heap)

    if v == 1:
        break

    if c > dp[v]:
        continue

    next_ = [v-1]

    if v % 3 == 0:
        next_.append(v // 3)

    if v % 2 == 0:
        next_.append(v // 2)

    for v_ in next_:
        sum_c = dp[v] + 1
        if dp[v_] > sum_c:
            dp[v_] = sum_c
            prev[v_] = v
            heappush(heap, (dp[v_], v_))

print(dp[1])

cur = 1
result = [str(cur)]
while prev[cur]:
    cur = prev[cur]
    result.append(str(cur))
print(" ".join(reversed(result)))