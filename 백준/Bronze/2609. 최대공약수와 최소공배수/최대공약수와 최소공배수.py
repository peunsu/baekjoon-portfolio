def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))