import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sum_A = [sum(A[i:j+1]) for i in range(n) for j in range(i, n)]
sum_B = [sum(B[i:j+1]) for i in range(m) for j in range(i, m)]

sum_B.sort()

cnt = 0
for a in sum_A:
    right = bisect_right(sum_B, t-a)
    left = bisect_left(sum_B, t-a)
    cnt += right - left
print(cnt)