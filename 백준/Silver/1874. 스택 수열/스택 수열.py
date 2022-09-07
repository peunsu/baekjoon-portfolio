n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
printer = ""

i = 0
for k, s in enumerate(seq):
    while True:
        if i < s:
            i += 1
            stack.append(i)
            printer += "+\n"
        else:
            if seq[k] != stack.pop():
                print("NO")
                exit(0)
            printer += "-\n"
            break
print(printer)