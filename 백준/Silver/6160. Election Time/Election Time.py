import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())

heap1, heap2 = [], []

for i in range(1, n+1):
    a, b = map(int, input().split())
    heappush(heap1, (-a, -b, i))

for _ in range(k):
    i, j, k = heappop(heap1)
    heappush(heap2, (j, k))

print(heappop(heap2)[1])