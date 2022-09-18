import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ear = set()
eye = set()

for _ in range(n):
    ear.add(input().rstrip())
for _ in range(m):
    eye.add(input().rstrip())

result = list(ear.intersection(eye))
result.sort()

print(len(result))
print("\n".join(result))