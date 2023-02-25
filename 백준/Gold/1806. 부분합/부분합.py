import sys
input = sys.stdin.readline

n, s = map(int, input().split())
seq = list(map(int, input().split()))

left = 0
right = 0
length = 1
min_length = float('inf')
total = seq[0]
while True:
    if total < s:
        right += 1
        length += 1
        if right >= n:
            break

        total += seq[right]
        if length > min_length:
            total -= seq[left]
            left += 1
            length = min_length
    else:
        total -= seq[left]
        left += 1
        min_length = length
        length -= 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)