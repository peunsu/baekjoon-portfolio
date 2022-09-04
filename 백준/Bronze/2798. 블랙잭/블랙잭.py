from itertools import combinations, takewhile

n, m = map(int, input().split())
cards = map(int, input().split())
cards_combi = combinations(cards, 3)
cards_sum = list(map(sum, cards_combi))
cards_sum.sort()
print(list(takewhile(lambda x: x <= m, cards_sum))[-1])