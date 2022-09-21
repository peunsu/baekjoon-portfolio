def visit_z(x: int, y: int, n: int):
    global cnt, r, c
    
    d = 2**(n-1)
    dc = 4**(n-1)
    
    if n:
        if r < y + d:
            if c < x + d:
                visit_z(x, y, n-1)
            else:
                cnt += dc
                visit_z(x+d, y, n-1)
        else:
            if c < x + d:
                cnt += dc * 2
                visit_z(x, y+d, n-1)
            else:
                cnt += dc * 3
                visit_z(x+d, y+d, n-1)
    else:
        if (x, y) == (c, r):
            print(cnt)
            exit(0)
        cnt += 1
            

n, r, c = map(int, input().split())

cnt = 0

visit_z(0, 0, n)