def tri(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

while(True):
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    if tri(a, b, c) or tri(a, c, b) or tri(b, c, a):
        print("right")
    else:
        print("wrong")