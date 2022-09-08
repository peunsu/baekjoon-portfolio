from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

print(round(sum(nums) / n))

nums.sort()
print(nums[(n-1)//2])

cnt = Counter(nums).most_common(2)
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
    
print(nums[-1] - nums[0])