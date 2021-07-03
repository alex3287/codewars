def corner_fill(square):
    size = len(square)
    R = []
    for i in range(size):
        A = square[i][:size - i]
        if len(square[0]) - i - 1:
            B = column(square, i)
            A += B
            if i % 2 != 0:
                A.reverse()
        R += A
    return R


def column(square, index):
    colum = len(square[0])
    rows = len(square)
    A = []
    for i in range(rows - index - 1):
        A.append(square[i+1+index][colum - index - 1])
    return A


M = [[1,2,3],
      [4,5,6],
      [7,8,9]]

print(corner_fill(M))
# [1, 2, 3, 6, 9, 8, 5, 4, 7]