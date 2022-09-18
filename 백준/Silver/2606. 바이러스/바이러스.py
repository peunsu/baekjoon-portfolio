import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

network = [list(map(int, input().split())) for _ in range(m)]

com = [1]
target = [1]

for t in target:
    for net in network:
        if t in net:
            net.remove(t)
            cur = net.pop()
            com.append(cur)
            target.append(cur)

print(len(set(com) - {1}))