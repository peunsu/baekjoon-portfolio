import sys
input = sys.stdin.readline

def trace_back(x, y):
    result = []

    while x > 0 and y > 0:
        if dp[x][y] == dp[x-1][y]:
            x -= 1
        elif dp[x][y] == dp[x][y-1]:
            y -= 1
        else:
            result.append(first[x-1])
            x -= 1
            y -= 1
    
    return result

first = input().rstrip()
second = input().rstrip()
len_first = len(first)
len_second = len(second)

dp = [[0] * (len_second + 1) for _ in range(len_first + 1)]

for i in range(1, len_first + 1):
    for j in range(1, len_second + 1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

lcs = trace_back(len_first, len_second)
print(len(lcs))
print("".join(reversed(lcs)))