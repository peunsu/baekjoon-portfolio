def visit_z(x: int, y: int, n: int):
    global cnt, r, c
    
    if n:
        if r < y + 2**(n-1):
            if c < x + 2**(n-1):
                visit_z(x, y, n-1)
            else:
                cnt += 4**(n-1)
                visit_z(x+2**(n-1), y, n-1)
        else:
            if c < x + 2**(n-1):
                cnt += 4**(n-1) * 2
                visit_z(x, y+2**(n-1), n-1)
            else:
                cnt += 4**(n-1) * 3
                visit_z(x+2**(n-1), y+2**(n-1), n-1)
    else:
        if (x, y) == (c, r):
            print(cnt)
            exit(0)
        cnt += 1
            

n, r, c = map(int, input().split())

cnt = 0

visit_z(0, 0, n)