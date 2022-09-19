from ntpath import join
import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    cnt = 0
    for i in range(n + 1):
        for j in range(n // 2 + 1):
            for k in range(n // 3 + 1):
                sum = i + j * 2 + k * 3
                num = math.factorial(i + j + k) // (math.factorial(i) * math.factorial(j) * math.factorial(k))
                if sum == n:
                    cnt += num

    print(cnt)