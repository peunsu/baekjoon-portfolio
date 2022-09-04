import sys

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    people.append([int(age), name])
people.sort(key=lambda x: x[0])
for age, name in people:
    print(age, name)