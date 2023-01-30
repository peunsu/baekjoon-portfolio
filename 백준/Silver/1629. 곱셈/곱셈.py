import sys, time
input = sys.stdin.readline

def multi(a: int, b: int):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return multi(a, b//2) ** 2 % c
    else:
        return multi(a, b//2) ** 2 * a % c

a, b, c = map(int, input().split())

print(multi(a, b))
