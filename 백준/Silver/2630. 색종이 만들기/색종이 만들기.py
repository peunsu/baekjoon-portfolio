import sys
from math import log2

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

cnt_w = 0
cnt_b = 0

nl = int(log2(n))
for k in range(nl + 1):
    for l in range(2**k):
        for m in range(2**k):
            sum_w = 0
            sum_b = 0
            for i in range(l * (2**(nl-k)), (l + 1) * (2**(nl-k))):
                for j in range(m * (2**(nl-k)), (m + 1) * (2**(nl-k))):
                    if visited[i][j]:
                        break
                    if arr[i][j] == 1:
                        sum_b += 1
                    else:
                        sum_w += 1
            if sum_w == 4**(nl-k):
                for i in range(l * (2**(nl-k)), (l + 1) * (2**(nl-k))):
                    for j in range(m * (2**(nl-k)), (m + 1) * (2**(nl-k))):
                        visited[i][j] = 1
                cnt_w += 1
            elif sum_b == 4**(nl-k):
                for i in range(l * (2**(nl-k)), (l + 1) * (2**(nl-k))):
                    for j in range(m * (2**(nl-k)), (m + 1) * (2**(nl-k))):
                        visited[i][j] = 1
                cnt_b += 1

print(cnt_w)
print(cnt_b)