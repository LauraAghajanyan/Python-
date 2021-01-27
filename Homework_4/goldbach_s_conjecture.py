def Prime(n):
    primes = list (range(2, n+1))
    for i in primes:
        j=2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    return primes

def odd(N):
    odd = Prime(N)
    odd.remove(2)
    return(odd)

def Goldbach(N):
    x, y = 0, 0
    result = 0
    if N % 2 == 0:
        prime = odd(N)
        while result != N:
            for i in range(len(prime)):
                if result == N:
                    break
                x = prime[i]
                for j in range(len(prime)):
                    y = prime[j]
                    result = x + y
                    if result == N:
                        break
    return x, y

N = int(input("Enter a number: "))
print(Goldbach(N))