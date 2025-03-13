import sys

input = sys.stdin.readline

def cross_product(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

def solution():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    
    s1 = cross_product(x2 - x1, y2 - y1, x3 - x2, y3 - y2) * cross_product(x2 - x1, y2 - y1, x4 - x2, y4 - y2)
    s2 = cross_product(x4 - x3, y4 - y3, x1 - x4, y1 - y4) * cross_product(x4 - x3, y4 - y3, x2 - x4, y2 - y4)
    
    if s1 == 0 and s2 == 0:
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        if x3 > x4:
            x3, x4 = x4, x3
        if y3 > y4:
            y3, y4 = y4, y3
        
        if x1 <= x4 and x3 <= x2 and y1 <= y4 and y3 <= y2:
            print(1)
        else:
            print(0)
        return
    
    if s1 <= 0 and s2 <= 0:
        print(1)
    else:
        print(0)
    
solution()