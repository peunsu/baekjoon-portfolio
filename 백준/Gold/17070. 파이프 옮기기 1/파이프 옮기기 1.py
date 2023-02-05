import sys
input = sys.stdin.readline


n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * (n) for _ in range(n)] for _ in range(3)]
# 0: 가로, 1: 세로, 2: 대각선

dp[0][0][1] = 1

for i in range(2, n):
    if home[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1, n):
    for j in range(2, n):
        if home[i][j] == 0 and home[i-1][j] == 0 and home[i][j-1] == 0:
            dp[2][i][j] = sum(dp[k][i-1][j-1] for k in range(3))
        if home[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]


print(sum(dp[k][n-1][n-1] for k in range(3)))