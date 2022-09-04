num = int(input())
for _ in range(num):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print(f"{h}{n//h:02d}")
    else:
        print(f"{n%h}{n//h + 1:02d}")