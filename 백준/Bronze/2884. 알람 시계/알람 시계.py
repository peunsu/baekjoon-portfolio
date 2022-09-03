hr, min = list(map(int, input().split()))

min = min - 45
if min < 0:
    min += 60
    hr -= 1
    if hr < 0:
        hr += 24

print(f"{hr} {min}")