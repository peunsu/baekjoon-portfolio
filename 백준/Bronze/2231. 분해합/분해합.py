import sys

input = sys.stdin.readline

n = int(input())

for i in range(max(n - len(str(n)) * 9, 1), n):
    total = i + sum(map(int, list(str(i))))
    if n == total:
        print(i)
        exit(0)
print(0)