import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [float('inf')] * 100001
dp[n] = 0

heap = []
heappush(heap, (0, n))
while heap:
    c, v = heappop(heap)

    if v == k:
        break

    if c > dp[v]:
        continue

    for c_, v_ in [(0, 2*v), (1, v-1), (1, v+1)]:
        if v_ < 0 or v_ > 100000:
            continue
        c_n = dp[v] + c_
        if dp[v_] > c_n:
            dp[v_] = c_n
            heappush(heap, (dp[v_], v_))

print(dp[k])