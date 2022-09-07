def check_prime(n: int):   
    if n == 1:
        return False
       
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True
        

m, n = map(int, input().split())
for i in range(m, n+1):
    if check_prime(i):
        print(i)