import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
sols = list(map(int, input().split()))

min_feature_value = float('inf')
min_sols = []
left = 0
right = n-1

while left < right:
    feature_value = sols[left] + sols[right]

    if abs(feature_value) < min_feature_value:
        min_feature_value = abs(feature_value)
        min_sols = [sols[left], sols[right]]
        if min_feature_value == 0:
            break
    
    if feature_value < 0:
        left += 1
    else:
        right -= 1

print(*sorted(min_sols))