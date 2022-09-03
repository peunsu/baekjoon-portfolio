word = input()
for i in range(ord('a'), ord('z') + 1):
    print(word.find(chr(i)), end=" ")