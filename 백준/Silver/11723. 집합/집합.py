import sys

input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    cmd = input().split()
    if cmd[0] == "add":
        s.add(int(cmd[1]))
    elif cmd[0] == "remove":
        if (x := int(cmd[1])) in s:
            s.remove(x)
    elif cmd[0] == "check":
        result = 1 if int(cmd[1]) in s else 0
        print(result)
    elif cmd[0] == "toggle":
        if (x := int(cmd[1])) in s:
            s.remove(x)
        else:
            s.add(x)
    elif cmd[0] == "all":
        s = {i for i in range(1, 21)}
    elif cmd[0] == "empty":
        s.clear()