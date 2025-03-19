import sys
input = sys.stdin.readline

n = int(input())

arr = [1, 2, 4, 7, 8, 11, 13, 14]

print(arr[(n-1)%8] + (n-1)//8*15)