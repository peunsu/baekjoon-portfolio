import sys

n = int(sys.stdin.readline())
nums = set([int(i) for i in sys.stdin.readline().split()])
m = int(sys.stdin.readline())
keys = [int(i) for i in sys.stdin.readline().split()]

for key in keys:
    if key in nums:
        print(1)
    else:
        print(0)