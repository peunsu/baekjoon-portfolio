import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def bisect_search(sorted, comparison) -> int:
    cnt = 0
    for a in comparison:
        right = bisect_right(sorted, t-a)
        left = bisect_left(sorted, t-a)
        cnt += right - left
    return cnt

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sum_A = [sum(A[i:j+1]) for i in range(n) for j in range(i, n)]
sum_B = [sum(B[i:j+1]) for i in range(m) for j in range(i, m)]

if n < m:
    sum_A.sort()
    ans = bisect_search(sum_A, sum_B)
else:
    sum_B.sort()
    ans = bisect_search(sum_B, sum_A)

print(ans)
