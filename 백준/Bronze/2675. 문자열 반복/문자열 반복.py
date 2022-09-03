length = int(input())
for _ in range(length):
    n, s = input().split()
    n = int(n)
    ans = []
    for i in range(len(s)):
        ans.append(s[i] * n)
    ans = "".join(ans)
    print(ans)