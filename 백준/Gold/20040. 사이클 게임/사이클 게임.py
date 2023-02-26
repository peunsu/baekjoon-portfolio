import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n)]

def find(x: int) -> int:
    if parents[x] == x:
        return x
    return find(parents[x])

def union(x: int, y: int) -> None:
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

for i in range(1, m+1):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i)
        break
else:
    print(0)