import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.append(points[0])

ans = abs(sum(points[i][0] * points[i+1][1] for i in range(n)) - sum(points[i][1] * points[i+1][0] for i in range(n))) / 2
print(round(ans, 1))