from collections import Counter
word = input().upper()
count = list(Counter(word).items())
count.sort(key=lambda x: x[1], reverse=True)
count = list(zip(*count))

if count[1].count(max(count[1])) > 1:
    print("?")
else :
    print(count[0][0])