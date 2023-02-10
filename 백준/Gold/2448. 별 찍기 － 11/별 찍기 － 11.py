class BaseStar():
    def __init__(self, n: int):
        self.star = [
            [" ", " ", "*", " ", " "],
            [" ", "*", " ", "*", " "],
            ["*", "*", "*", "*", "*"]
        ]
        self.k = 3
        self.n = n
    
    def expand_base_star(self):
        for i in range(self.k):
            line = self.star[i]
            self.star.append(line + [" "] + line)
            self.star[i] = [" "] * self.k + line + [" "] * self.k
        self.k *= 2

    def make_star(self):
        while self.k < self.n:
            self.expand_base_star()

    def print_star(self):
        self.make_star()

        for star in self.star:
            print("".join(star))

n = int(input())
base_star = BaseStar(n)

base_star.print_star()