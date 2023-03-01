import sys
from collections import defaultdict
input = sys.stdin.readline

def count_cases(A, B) -> int:
    cnt = 0
    for a in A:
        if (b := t - a) in B:
            cnt += A[a] * B[b]
    return cnt

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sum_A = defaultdict(int)
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += A[j]
        sum_A[temp] += 1

sum_B = defaultdict(int)
for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += B[j]
        sum_B[temp] += 1

ans = count_cases(sum_A, sum_B)

print(ans)
