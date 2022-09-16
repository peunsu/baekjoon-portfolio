import sys
sys.setrecursionlimit(10**6)

def finder(s: int, t: int, arr: list):
    arr[t][s] = 0
    
    if s + 1 < m and arr[t][s+1] == 1:
        finder(s+1, t, arr)
    if t + 1 < n and arr[t+1][s] == 1:
        finder(s, t+1, arr)
    if s - 1 >= 0 and arr[t][s-1] == 1:
        finder(s-1, t, arr)
    if t - 1 >= 0 and arr[t-1][s] == 1:
        finder(s, t-1, arr)

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[j][i] == 1:
                finder(i, j, arr)
                cnt += 1
    
    print(cnt)