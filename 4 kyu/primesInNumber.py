def primeFactors(n):
    result = ''
    prime = 2
    while n > 1:
        k = 0
        while n % prime == 0:
            n //= prime
            k += 1
        if k:
            if k == 1:
                result += '('+str(prime)+')'
            else:
                result += '('+str(prime)+'**'+str(k)+')'
        prime = nextPrime(prime)
    return result

def nextPrime(prime):
    A = [i for i in range(1000000)]
    n = 2
    R = []
    i = 0
    while n < 1000000:
        if A[n] != 0:
            R.append(A[n])
            i += 1
            for i in range(n, 1000000, n):
                A[i] = 0
        n += 1
    return R[R.index(prime)+1]

def stream():
    n = 10000000
    a = list(range(n + 1))
    a[1] = 0

    i = 2
    while i <= n:
        if a[i] != 0:
            yield a[i]
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1

print(nextPrime(71))
print(primeFactors(35791357))
