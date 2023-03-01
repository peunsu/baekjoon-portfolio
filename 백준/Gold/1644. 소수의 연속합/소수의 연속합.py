import sys
input = sys.stdin.readline

def prime_number(max_num):
    prime = [1] * (max_num+1)
    prime[0], prime[1] = 0, 0

    for i in range(2, int(max_num**0.5)+1):
        if prime[i]:
            for j in range(i*2, max_num+1, i):
                prime[j] = 0
    return [i for i in range(2, max_num+1) if prime[i]]

prime_nums = prime_number(4_000_000)

n = int(input())

left, right = 0, 0
total = prime_nums[0]
cnt = 0
while left <= right:
    if total < n:
        right += 1
        if right >= len(prime_nums):
            break
        total += prime_nums[right]
    elif total > n:
        total -= prime_nums[left]
        left += 1
    else:
        cnt += 1
        total -= prime_nums[left]
        left += 1

print(cnt)