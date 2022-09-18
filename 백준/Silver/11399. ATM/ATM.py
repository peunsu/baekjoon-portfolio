import sys
from itertools import accumulate

input = sys.stdin.readline

n = int(input())
ps = list(map(int, input().split()))
ps.sort()
print(sum(accumulate(ps)))
