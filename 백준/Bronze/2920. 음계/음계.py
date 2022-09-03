nums = list(map(int, input().split()))

if nums == list(sorted(nums)):
    print("ascending")
elif nums == list(sorted(nums, reverse=True)):
    print("descending")
else:
    print("mixed")