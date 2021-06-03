def variants(word):
    n = len(word)
    sample = sorted(word)
    return sample
    A = list(word)
    if A == sample:
        return 1
    count = 0
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                count += 1
                if A == sample:
                    return count+1
    return sample

def listPosition(word):
    if len(word) < 2:
        return 1
    return variants(word)


print(listPosition('QUESTION'))

