n = int(input())

chess = [0] * n
cnt = 0

def check(x: int):
    for i in range(x):
        if chess[i] == chess[x] or abs(chess[i] - chess[x]) == abs(i - x):
            return False
    return True

def place_chess(x: int):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        chess[x] = i
        if check(x):
            place_chess(x+1)

place_chess(0)

print(cnt)