a, b, c = [int(input()) for _ in range(3)]
s = list(str(a * b * c))
for i in range(10):
    print(s.count(str(i)))