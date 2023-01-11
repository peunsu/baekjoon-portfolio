import sys

input = sys.stdin.readline

def paper(x: int, y: int, n: int):
    start = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != start:
                for p in [x, x + n//3, x + 2*n//3]:
                    for q in [y, y + n//3, y + 2*n//3]:
                        paper(p, q, n//3)
                return

    if start == -1:
        cnt[0] += 1
    elif start == 0:
        cnt[1] += 1
    else:
        cnt[2] += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0, 0]

paper(0, 0, n)

for c in cnt:
    print(c)