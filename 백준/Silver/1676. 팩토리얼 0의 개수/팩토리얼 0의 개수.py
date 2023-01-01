from math import factorial

n = int(input())
fact = str(factorial(n))

print(len(fact) - len(fact.rstrip("0")))