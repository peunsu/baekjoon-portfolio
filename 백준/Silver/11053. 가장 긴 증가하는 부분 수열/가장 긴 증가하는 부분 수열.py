import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1
        else:
            dp[i] = max(1, dp[i])

print(max(dp))