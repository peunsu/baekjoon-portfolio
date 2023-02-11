string = input()
explosion = input()

len_explosion = len(explosion)

stack = []
for s in string:
    stack.append(s)
    if "".join(stack[-len_explosion:]) == explosion:
        for _ in range(len_explosion):
            stack.pop()

print("".join(stack) if stack else "FRULA")