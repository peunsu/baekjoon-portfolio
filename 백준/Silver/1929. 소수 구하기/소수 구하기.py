prime = {1: False}

def check_prime(n: int):
    if n in prime.keys():
        return prime[n]
      
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime[n] = False
            return False
    
    prime[n] = True
    return True
        

m, n = map(int, input().split())
for i in range(m, n+1):
    if check_prime(i):
        print(i)