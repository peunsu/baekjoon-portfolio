import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bag_max_weight = [int(input()) for _ in range(k)]

heapify(gems)
bag_max_weight.sort()

total = 0
gems_candidate = []
for i in range(k):
    while gems and bag_max_weight[i] >= gems[0][0]:
        m, v = heappop(gems)
        heappush(gems_candidate, -v)

    if gems_candidate:
        max_v_neg = heappop(gems_candidate)
        total -= max_v_neg

print(total)