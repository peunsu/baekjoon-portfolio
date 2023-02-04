from itertools import chain

first = input()
second = input()

first_len = len(first)
second_len = len(second)

dp = [[0] * (second_len + 1) for _ in range(first_len + 1)]

for i in range(first_len):
    for j in range(second_len):
        if first[i] == second[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(max(chain(*dp)))