import sys
from bisect import bisect_left

input = sys.stdin.readline

def solution():
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    dp_len = [0] * (n+1)
    dp_max = [1_000_000] * (n+1)
    dp_max[0] = 0
    
    for i in range(1, n+1):
        idx = bisect_left(dp_max, arr[i])
        dp_len[i] = idx
        dp_max[idx] = arr[i]
    
    print(max(dp_len))

solution()