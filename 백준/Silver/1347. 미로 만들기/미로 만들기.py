import sys
input = sys.stdin.readline

n = int(input())
note = list(input().rstrip())

pos = [(0, 0)]
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]
v = 0

for i in note:
    if i == "R":
        v = (v - 1 + 4) % 4
    elif i == "L":
        v = (v + 1) % 4
    elif i == "F":
        pos.append((pos[-1][0] + vector[v][0], pos[-1][1] + vector[v][1]))

min_pos = [min(pos, key=lambda x: x[0])[0], min(pos, key=lambda x: x[1])[1]]
max_pos = [max(pos, key=lambda x: x[0])[0], max(pos, key=lambda x: x[1])[1]]

pos = list(map(lambda x: (x[0] - min_pos[0], x[1] - min_pos[1]), pos))
size = (max_pos[0] - min_pos[0] + 1, max_pos[1] - min_pos[1] + 1)

arr = [["#" for _ in range(size[1])] for _ in range(size[0])]
for x, y in pos:
    arr[x][y] = "."

print("\n".join(["".join(i) for i in arr]))