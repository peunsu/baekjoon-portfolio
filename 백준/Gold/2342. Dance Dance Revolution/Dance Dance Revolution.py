import sys
input = sys.stdin.readline

def calc_pow(x, k):
    if x == 0:
        return 2
    diff = abs(x-k)
    if diff == 0:
        return 1
    elif diff % 2 == 0:
        return 4
    else:
        return 3

seq = list(map(int, input().split()))[:-1]
n = len(seq)
dp = [[[float('inf')] * (5) for _ in range(5)] for _ in range(len(seq) + 1)]
dp[0][0][0] = 0

for i in range(n):
    k = seq[i]
    for x in range(5):
        for y in range(5):
            if x != k:
                power = calc_pow(y, k)
                dp[i+1][x][k] = min(dp[i+1][x][k], dp[i][x][y] + power)
            if y != k:
                power = calc_pow(x, k)
                dp[i+1][k][y] = min(dp[i+1][k][y], dp[i][x][y] + power)

min_pow = float('inf')
for i in range(5):
    for j in range(5):
        min_pow = min(min_pow, dp[n][i][j])

print(min_pow)