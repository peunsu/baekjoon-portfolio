import sys
input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))

dp_left = [1] * n
dp_right = [1] * n

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i] and dp_left[j] >= dp_left[i]:
            dp_left[i] = dp_left[j] + 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if nums[j] < nums[i] and dp_right[j] >= dp_right[i]:
            dp_right[i] = dp_right[j] + 1

dp = [a+b-1 for a, b in zip(dp_left, dp_right)]
print(max(dp))