k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]

left, right = 1, max(length)
while left <= right:
    middle = (left + right) // 2
    if sum(map(lambda x: x//middle, length)) < n:
        right = middle - 1
    else:
        left = middle + 1
print(right)