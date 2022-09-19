n = int(input())
nums = list(map(int, input().split()))
nums_s = sorted(list(set(nums)))
nums_d = {}
for i, n in enumerate(nums_s):
    nums_d[n] = i

for n in nums:
    print(nums_d[n], end=" ")