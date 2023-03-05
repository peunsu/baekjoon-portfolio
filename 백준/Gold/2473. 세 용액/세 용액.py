import sys
input = sys.stdin.readline

n = int(input())
sols = list(map(int, input().split()))
sols.sort()

min_total = float('inf')
min_sols = list()

for i in range(n-2):
    left, right = i+1, n-1
    while left < right:
        total = sols[i] + sols[left] + sols[right]
        abs_total = abs(total)
        if min_total > abs_total:
            min_total = abs_total
            min_sols = [sols[i], sols[left], sols[right]]

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            break
            
print(*sorted(min_sols))