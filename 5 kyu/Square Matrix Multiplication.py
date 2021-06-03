def matrix_mult(a, b):
    n = len(a)
    c = [[] for i in range(n)]
    for i in range(n):
        row = a[i]
        for j in range(n):
            col = get_column(b, j)
            temp = 0
            for k in range(n):
                temp += (row[k]*col[k])
            c[i].append(temp)
    return c


def get_column(arr, n):
    column = []
    for i in arr:
        column.append(i[n])
    return column


a = [ [1, 2, 3],
    [3, 2, 1],
    [2, 1, 3] ]
#       x
b =  [ [4, 5, 6],
    [6, 5, 4],
    [4, 6, 5] ]
print(matrix_mult(a, b))

#        =
#   [ [28, 33, 29],
#     [28, 31, 31],
#     [26, 33, 31] ])