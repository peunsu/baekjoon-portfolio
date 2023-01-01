from heapq import heappush, heappop, heapify, nlargest
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    heap_min = []
    heap_max = []
    ids = [0] * 1_000_001
    k = int(input())
    for i in range(k):
        cmd = input().split()
        if cmd[0] == "I":
            heappush(heap_min, (int(cmd[1]), i))
            heappush(heap_max, (-int(cmd[1]), i))
            ids[i] = 1
        elif cmd[0] == "D":
            if cmd[1] == "1":
                while heap_max and not ids[heap_max[0][1]]:
                    heappop(heap_max)
                if heap_max:
                    ids[heappop(heap_max)[1]] = 0
            else:
                while heap_min and not ids[heap_min[0][1]]:
                    heappop(heap_min)
                if heap_min:
                    ids[heappop(heap_min)[1]] = 0

    while heap_max and not ids[heap_max[0][1]]:
        heappop(heap_max)
    while heap_min and not ids[heap_min[0][1]]:
        heappop(heap_min)

    if heap_min and heap_max:
        print(-heap_max[0][0], heap_min[0][0])
    else:
        print("EMPTY")