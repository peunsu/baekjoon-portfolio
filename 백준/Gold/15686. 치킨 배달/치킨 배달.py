import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

min_dist = float('inf')
for chicken in combinations(chickens, m):
    chicken_dist = sum([min([abs(i - u) + abs(j - v) for u, v in chicken]) for i, j in houses])
    if chicken_dist < min_dist: min_dist = chicken_dist

print(min_dist)