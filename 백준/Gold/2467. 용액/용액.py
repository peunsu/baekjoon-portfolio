import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
sols = list(map(int, input().split()))

min_feature_value = float('inf')
min_sols = []
for sol in sols:
    idx = bisect_left(sols, -sol)
    a, b = idx-1, idx
    for k in a, b:
        if not 0 <= k < n:
            continue
        if sols[k] == sol:
            continue
        feature_value = abs(sol + sols[k])
        if feature_value == 0:
            min_sols = [sol, sols[k]]
            break
        if min_feature_value > feature_value:
            min_feature_value = feature_value
            min_sols = [sol, sols[k]]

print(*sorted(min_sols))