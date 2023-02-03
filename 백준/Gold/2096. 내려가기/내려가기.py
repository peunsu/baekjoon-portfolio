import sys
input = sys.stdin.readline

n = int(input())

window_max = [[0, 0, 0], [0, 0, 0]]
window_min = [[0, 0, 0], [0, 0, 0]]

for i in range(n):
    nums = list(map(int, input().split()))

    if i == 0:
        window_max[0] = nums.copy()
        window_min[0] = nums.copy()
        continue
    
    window_max[1] = nums.copy()
    window_max[1][0] += max(window_max[0][:2])
    window_max[1][1] += max(window_max[0])
    window_max[1][2] += max(window_max[0][1:])
    window_max[0] = window_max[1]

    window_min[1] = nums.copy()
    window_min[1][0] += min(window_min[0][:2])
    window_min[1][1] += min(window_min[0])
    window_min[1][2] += min(window_min[0][1:])
    window_min[0] = window_min[1]

print(max(window_max[0]), min(window_min[0]))