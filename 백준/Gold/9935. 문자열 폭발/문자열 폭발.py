string = input()
explosion = input()

last_explosion = explosion[-1]
len_explosion = len(explosion)

stack = []
for s in string:
    stack.append(s)
    if s == last_explosion and "".join(stack[-len_explosion:]) == explosion:
        del(stack[-len_explosion:])

print("".join(stack) if stack else "FRULA")