import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    minv = 1000000
    
    for j in range(1, int(i**0.5) + 1):
        minv = min(minv, dp[i - j**2])
    dp[i] = minv + 1

print(dp[n])