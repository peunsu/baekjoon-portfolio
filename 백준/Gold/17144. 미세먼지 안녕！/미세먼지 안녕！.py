import sys
from operator import add
input = sys.stdin.readline

def diffuse():
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if smog[i][j] > 0:
                diff = smog[i][j] // 5
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i+x < r and 0 <= j+y < c and smog[i+x][j+y] != -1:
                        temp[i+x][j+y] += diff
                        temp[i][j] -= diff

    for i in range(r):
        for j in range(c):
            smog[i][j] += temp[i][j]

def clean_up():
    for i in range(1, c):
        if i == 1:
            prev_ = 0
        else:
            prev_ = cur_
        
        cur_ = smog[cleaner[0]][i]
        smog[cleaner[0]][i] = prev_
    
    for i in range(cleaner[0]-1, -1, -1):
        prev_ = cur_
        cur_ = smog[i][c-1]
        smog[i][c-1] = prev_

    for i in range(c-2, -1, -1):
        prev_ = cur_
        cur_ = smog[0][i]
        smog[0][i] = prev_

    for i in range(1, cleaner[0]):
        prev_ = cur_
        cur_ = smog[i][0]
        smog[i][0] = prev_

def clean_down():
    for i in range(1, c):
        if i == 1:
            prev_ = 0
        else:
            prev_ = cur_
        
        cur_ = smog[cleaner[1]][i]
        smog[cleaner[1]][i] = prev_
    
    for i in range(cleaner[1]+1, r):
        prev_ = cur_
        cur_ = smog[i][c-1]
        smog[i][c-1] = prev_

    for i in range(c-2, -1, -1):
        prev_ = cur_
        cur_ = smog[r-1][i]
        smog[r-1][i] = prev_

    for i in range(r-2, cleaner[1], -1):
        prev_ = cur_
        cur_ = smog[i][0]
        smog[i][0] = prev_

r, c, t = map(int, input().split())
smog = [list(map(int, input().split())) for _ in range(r)]
cleaner = []

for i in range(2, r-2):
    if smog[i][0] == -1:
        cleaner.append(i)

for _ in range(t):
    diffuse()
    clean_up()
    clean_down()

total = 0
for i in range(r):
    for j in range(c):
        total += smog[i][j]
print(total+2)