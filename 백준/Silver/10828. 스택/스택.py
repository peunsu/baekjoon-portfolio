import sys
from collections import deque

deq = deque()

n = int(input())
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        deq.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if not deq:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if deq:
            print(deq[-1])
        else:
            print(-1)