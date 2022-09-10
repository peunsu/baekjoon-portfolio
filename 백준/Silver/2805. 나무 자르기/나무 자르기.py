import sys

input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))

left, right = 0, max(height)
while left <= right:
    h = (left + right) // 2
    diff = [he - h if he > h else 0 for he in height]
    if sum(diff) >= m:
        left = h + 1
    else:
        right = h - 1
print(right)