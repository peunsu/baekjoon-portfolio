import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = input().strip("[]\n").split(",")
    arr = deque() if arr == [''] else deque(arr)

    reverse = False
    for pp in p:
        if pp == "R":
            reverse = not reverse
            continue

        if not arr:
            print("error")
            break

        arr.pop() if reverse else arr.popleft()
    else:
        if reverse: arr.reverse()
        print(f"[{','.join(arr)}]")
