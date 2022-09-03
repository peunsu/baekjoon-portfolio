num = int(input())
for _ in range(num):
    ox = input()
    score, total = 1, 0
    for s in ox:
        if s == "O":
            total += score
            score += 1
        elif s == "X":
            score = 1
    print(total)