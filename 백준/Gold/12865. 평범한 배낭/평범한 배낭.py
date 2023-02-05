import sys
input = sys.stdin.readline

n, k = map(int, input().split())

things = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < things[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-things[i-1][0]] + things[i-1][1])

print(dp[n][k])