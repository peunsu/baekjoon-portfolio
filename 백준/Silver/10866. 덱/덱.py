import sys
from collections import deque

deq = deque()

n = int(input())
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        deq.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        deq.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd[0] == "pop_back":
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
    elif cmd[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)