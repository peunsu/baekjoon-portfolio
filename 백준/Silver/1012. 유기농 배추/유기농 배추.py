import sys
sys.setrecursionlimit(10**6)

def finder(x: int, y: int, arr: list) -> bool:
    if (target := (x + 1, y)) in arr:
        arr.remove(target)
        finder(*target, arr)
    if (target := (x - 1, y)) in arr:
        arr.remove(target)
        finder(*target, arr)
    if (target := (x, y + 1)) in arr:
        arr.remove(target)
        finder(*target, arr)
    if (target := (x, y - 1)) in arr:
        arr.remove(target)
        finder(*target, arr)

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(k)]
    
    cnt = 0
    while arr:
        x, y = arr.pop(0)
        finder(x, y, arr)
        cnt += 1
    
    print(cnt)