def prime(n):
    A = [i for i in range(n+1)]
    k = 2
    R = []
    i = 0
    while k < (n+1):
        if A[k] != 0:
            R.append(A[k])
            i += 1
            for i in range(k, (n+1), k):
                A[i] = 0
        k += 1
    return R


n = 34
print(prime(n))