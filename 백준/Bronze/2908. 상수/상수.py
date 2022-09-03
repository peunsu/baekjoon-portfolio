n1, n2 = input().split()
n1 = n1[::-1]
n2 = n2[::-1]
print(n1 if int(n1) > int(n2) else n2)