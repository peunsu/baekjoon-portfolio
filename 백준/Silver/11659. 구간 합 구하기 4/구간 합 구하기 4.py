import sys
from itertools import accumulate

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
acc = list(accumulate(nums))

for _ in range(m):
    i, j = map(int, input().split())
    if i > 1:
        print(acc[j-1] - acc[i-2])
    else:
        print(acc[j-1])