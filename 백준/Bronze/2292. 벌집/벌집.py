n = int(input())

a, b = 1, 1
i = 1
while True:
    if a <= n <= b:
        print(i)
        break
    else:
        a = b + 1
        b = b + i * 6
        i += 1