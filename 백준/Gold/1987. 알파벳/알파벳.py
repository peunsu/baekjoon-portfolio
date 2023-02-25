import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]
visited = [0] * 26

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

max_cnt = 0

def dfs(x: int, y: int, cnt: int):
    global max_cnt

    if cnt > max_cnt:
        max_cnt = cnt

    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < r and 0 <= y_ < c and not visited[board[x_][y_]]:
            visited[board[x_][y_]] = 1
            dfs(x_, y_, cnt + 1)
            visited[board[x_][y_]] = 0

visited[board[0][0]] = 1
dfs(0, 0, 1)

print(max_cnt)