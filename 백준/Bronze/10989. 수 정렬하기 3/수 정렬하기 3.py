import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = defaultdict(lambda: 0)
for _ in range(n):
    nums[int(input())] += 1
for i in range(10001):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)