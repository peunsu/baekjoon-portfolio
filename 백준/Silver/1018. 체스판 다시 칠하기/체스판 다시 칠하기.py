n, m = map(int, input().split())
chess = [[1 if c == "W" else -1 for c in input()] for _ in range(n)]
count = []
for a in range(0, n-7):
    for b in range(0, m-7):
        cnt1, cnt2 = 0, 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if chess[i][j] != (-1)**(i+j):
                    cnt1 += 1
                elif chess[i][j] != (-1)**(i+j-1):
                    cnt2 += 1
        count.append(min(cnt1, cnt2))
print(min(count))