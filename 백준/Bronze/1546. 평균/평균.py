num = int(input())
score = list(map(int, input().split()))
m = max(score)
score = [s/m*100 for s in score]
print(sum(score)/num)