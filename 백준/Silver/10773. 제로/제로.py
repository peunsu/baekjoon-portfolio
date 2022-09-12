import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
stack = deque()

for _ in range(n):
    if (i := int(input())) != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))