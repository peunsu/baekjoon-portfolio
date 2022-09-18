import sys

input = sys.stdin.readline

n = int(input())
fibo = [1, 1] + [0] * (n-1)

for i in range(1, n+1):
    if fibo[i]:
        continue
    fibo[i] = fibo[i-2] + fibo[i-1]

print(fibo[n] % 10007)