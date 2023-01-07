import sys
from math import factorial

input = sys.stdin.readline

n = int(input())
sum = 0

for i in range(n//2 + 1):
    temp = (factorial(n-i) // (factorial(i) * factorial(n-2*i))) * (2 ** i)
    sum += temp
print(sum % 10007)