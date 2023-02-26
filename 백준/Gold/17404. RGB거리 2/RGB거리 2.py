import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
result = float('inf')

for k in range(3):
    dp = [[float('inf')] * 3 for _ in range(n)]
    dp[0][k] = cost[0][k]
    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    for i in range(3):
        if k != i:
            result = min(result, dp[n-1][i])

print(result)