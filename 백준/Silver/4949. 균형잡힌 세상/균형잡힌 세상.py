from collections import deque

while True:
    mystr = input()
    if mystr == ".":
        break
    stack = deque()
    for s in mystr:
        if s == "(":
            stack.append(0)
        elif s == ")":
            try:
                if stack.pop() != 0:
                    break
            except:
                break
        elif s == "[":
            stack.append(1)
        elif s == "]":
            try:
                if stack.pop() != 1:
                    break
            except:
                break
    else:
        if not stack:
            print("yes")
            continue
    print("no")
    