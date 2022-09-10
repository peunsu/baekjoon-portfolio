n = int(input())

ls = set()
for i in range(n // 3 + 1):
    for j in range(n // 5 + 1):
        if 3 * i + 5 * j == n:
            ls.add(i+j)
if ls:
    print(min(ls))
else:
    print(-1)