equation = input().split("-")

tot = 0

for eq in equation[0].split("+"):
    tot += int(eq)
    
for eq in equation[1:]:
    for e in eq.split("+"):
        tot -= int(e)

print(tot)