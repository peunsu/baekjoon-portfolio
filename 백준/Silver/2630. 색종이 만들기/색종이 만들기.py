import sys

input = sys.stdin.readline
cnt_w = 0
cnt_b = 0

def cutter(x, y, size):
    global cnt_w, cnt_b

    if x >= k or y >= k:
        return

    pt = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != pt:
                cutter(x, y, size//2)
                cutter(x + size//2, y, size//2)
                cutter(x, y+size//2, size//2)
                cutter(x + size//2, y + size//2, size//2)
                return
    if pt:
        cnt_b += 1
    else:
        cnt_w += 1

k = int(input())
paper = [list(map(int, input().split())) for _ in range(k)]

cutter(0, 0, k)
print(cnt_w)
print(cnt_b)