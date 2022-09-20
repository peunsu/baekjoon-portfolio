import sys

input = sys.stdin.readline

cnt_w, cnt_b = 0, 0

def paper(x: int, y: int, n: int):
    global cnt_w, cnt_b

    start = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != start:
                paper(x, y, n//2)
                paper(x+n//2, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y+n//2, n//2)
                return
    
    if start:
        cnt_b += 1
    else:
        cnt_w += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

paper(0, 0, n)

print(cnt_w)
print(cnt_b)