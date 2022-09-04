import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().split())

count = Counter(cards)
for num in nums:
    print(count[num], end=" ")