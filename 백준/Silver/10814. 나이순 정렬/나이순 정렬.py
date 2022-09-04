n = int(input())
people = [input().split() for i in range(n)]
people = [[int(age), name] for [age, name] in people]
people.sort(key=lambda x: x[0])
for person in people:
    print(*person)