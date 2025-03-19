import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trains = [0] * (n+1)

for _ in range(m):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 1:
        trains[cmd[1]] |= 1 << cmd[2]
    elif cmd[0] == 2:
        trains[cmd[1]] &= ~(1 << cmd[2])
    elif cmd[0] == 3:
        trains[cmd[1]] <<= 1
        trains[cmd[1]] &= (1 << 21) - 1
    elif cmd[0] == 4:
        trains[cmd[1]] >>= 1
        trains[cmd[1]] &= ~1

print(len(set(trains[1:])))