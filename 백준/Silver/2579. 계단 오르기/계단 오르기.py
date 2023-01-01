import sys

input = sys.stdin.readline

n = int(input())

score = [int(input()) for _ in range(n)] + [0] * (300-n)
tot = [0] * 300

tot[0] = score[0]
tot[1] = max(score[0] + score[1], score[1])
tot[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, n):
    tot[i] = max(tot[i-2] + score[i], tot[i-3] + score[i-1] + score[i])

print(tot[n-1])