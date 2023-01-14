import sys

input = sys.stdin.readline

result = []

def quadtree(x: int, y: int, n: int):
    start = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != start:
                result.append("(")
                quadtree(x, y, n//2)
                quadtree(x, y+n//2, n//2)
                quadtree(x+n//2, y, n//2)
                quadtree(x+n//2, y+n//2, n//2)
                result.append(")")
                return
    result.append(start)
    

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

quadtree(0, 0, n)
print("".join(result))