n = int(input())

num = 0
while n >= 0:
    if n % 5 == 0:
        num += n // 5
        print(num)
        break
    else:
        n -= 3
        num += 1
else:
    print(-1)