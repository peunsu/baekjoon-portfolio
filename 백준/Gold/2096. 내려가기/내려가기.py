import sys
input = sys.stdin.readline

def find_min() -> int:
    window = [[0, 0, 0], [0, 0, 0]]
    window[0] = nums[0][:]
    for i in range(1, n):
        window[1] = nums[i][:]
        window[1][0] += min(window[0][:2])
        window[1][1] += min(window[0])
        window[1][2] += min(window[0][1:])
        window[0] = window[1]
    return min(window[0])

def find_max() -> int:
    window = [[0, 0, 0], [0, 0, 0]]
    window[0] = nums[0][:]
    for i in range(1, n):
        window[1] = nums[i][:]
        window[1][0] += max(window[0][:2])
        window[1][1] += max(window[0])
        window[1][2] += max(window[0][1:])
        window[0] = window[1]
    return max(window[0])

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

print(find_max(), find_min())