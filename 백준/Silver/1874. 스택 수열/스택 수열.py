n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
printer = []

i = 0
for s in seq:
    while True:
        if i < s:
            i += 1
            stack.append(i)
            printer.append("+")
        else:
            if s != stack.pop():
                print("NO")
                exit(0)
            printer.append("-")
            break
print("\n".join(printer))