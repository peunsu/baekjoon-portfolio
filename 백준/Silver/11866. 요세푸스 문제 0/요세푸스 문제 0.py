from collections import deque

n, k = map(int, input().split())
people = deque([i for i in range(1, n+1)])
result = []
for i in range(n):
    people.rotate(-(k-1))
    result.append(people.popleft())
print(f"<{str(result)[1:-1]}>")