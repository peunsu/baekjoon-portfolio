import sys
from itertools import accumulate
from operator import add
input = sys.stdin.readline

n, m = map(int, input().split())
acc = [[0] * (n+1)]

for i in range(1, n+1):
    acc.append(list(map(add, [0] + list(accumulate(map(int, input().split()))), acc[i-1])))

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(acc[x2][y2] - acc[x2][y1-1] - acc[x1-1][y2] + acc[x1-1][y1-1])