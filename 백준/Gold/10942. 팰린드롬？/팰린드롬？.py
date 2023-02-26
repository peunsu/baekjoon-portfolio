import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1
for cnt in range(2, n+1):
    for i in range(n-cnt):
        j = i + cnt
        if nums[i] == nums[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])