import sys

n = int(sys.stdin.readline())
for _ in range(n):
    ps = sys.stdin.readline().rstrip()
    while ps.find("()") != -1:
        ps = ps.replace("()", "")
    if ps:
        print("NO")
    else:
        print("YES")
    