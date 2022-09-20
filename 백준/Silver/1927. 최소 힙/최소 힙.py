import sys

input = sys.stdin.readline

n = int(input())
arr = [0]

for _ in range(n):
    x = int(input())

    if x:
        arr.append(x)
        cur = len(arr) - 1
        while cur > 1 and arr[cur] < arr[cur//2]:
            arr[cur], arr[cur//2] = arr[cur//2], arr[cur]
            cur //= 2
    else:
        if len(arr) == 1:
            print(0)
            continue

        arr[-1], arr[1] = arr[1], arr[-1]
        print(arr.pop())
        
        cur = 1
        while True:
            next = cur * 2
            if next + 1 < len(arr) and arr[next + 1] < arr[next]:
                next += 1
            if next >= len(arr) or arr[next] >= arr[cur]:
                break
            arr[next], arr[cur] = arr[cur], arr[next]
            cur = next