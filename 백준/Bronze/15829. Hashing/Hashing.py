l = int(input())
word = [ord(i) - 96 for i in list(input())]
hash = 0
for i, w in enumerate(word):
    hash += w * (31 ** i)
print(hash % 1234567891)