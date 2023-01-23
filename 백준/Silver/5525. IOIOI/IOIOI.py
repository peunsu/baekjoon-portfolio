import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

key = "I" + n * "OI"

cnt = 0
start = 0
while start < m:
    start = s.find(key, start) + 1
    if start == 0:
        break
    cnt += 1

print(cnt)