equation = input()

nums = []
operators = []

s = 0
for i, eq in enumerate(equation):
    if not eq.isnumeric():
        nums.append(int(equation[s:i]))
        operators.append(equation[i])
        s = i + 1
    if i == len(equation) - 1:
        nums.append(int(equation[s:]))

for i, op in enumerate(operators):
    if op == "-":
        nums[i+1:] = [-n for n in nums[i+1:]]
        break

print(sum(nums))