n = int(input())
nums = list(map(int, input().split()))
nums_s = sorted(set(nums))
nums_d = {n: i for i, n in enumerate(nums_s)}

print(" ".join([str(nums_d[n]) for n in nums]))