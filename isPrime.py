

def isPrime (n):
    for a in range(2,n):
        if n%a==0:
            return (n,"is not a prime no ")
    return(n,"is a prime no ")

print(isPrime(5))
