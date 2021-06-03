def multiplication_table(size):
    A = []
    B = []
    for i in range(size):
        for j in range(size):
            B.append((i+1)*(j+1))
        A.append(B)
        B = []
    return A


print(multiplication_table(5))