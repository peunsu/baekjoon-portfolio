import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pw = dict()
for _ in range(n):
    i, j = input().split()
    pw[i] = j

ans = []
for _ in range(m):
    addr = input().rstrip()
    ans.append(pw[addr])

print("\n".join(ans))