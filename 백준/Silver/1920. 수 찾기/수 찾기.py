from collections import Counter
import sys

n = int(sys.stdin.readline())
nums = [int(i) for i in sys.stdin.readline().split()]
m = int(sys.stdin.readline())
keys = [int(i) for i in sys.stdin.readline().split()]

count = Counter(nums)
for key in keys:
    if count[key] != 0:
        print(1)
    else:
        print(0)