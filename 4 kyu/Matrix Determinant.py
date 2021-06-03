# Ok
def binar(arr):
    return arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]


def three(arr):
    return arr[0][0] * (arr[1][1] * arr[2][2] - arr[1][2] * arr[2][1]) - arr[0][1] * (
                arr[1][0] * arr[2][2] - arr[1][2] * arr[2][0]) + arr[0][2] * (
                       arr[1][0] * arr[2][1] - arr[1][1] * arr[2][0])


def four(arr):
    A = [i[1:] for i in arr[1:]]
    B = [i[:1] + i[2:] for i in arr[1:]]
    C = [i[:2] + i[3:] for i in arr[1:]]
    D = [i[:-1] for i in arr[1:]]
    return arr[0][0] * three(A) - arr[0][1] * three(B) + arr[0][2] * three(C) - arr[0][3] * three(D)

def five(arr):
    A = [i[1:] for i in arr[1:]]
    B = [i[:1] + i[2:] for i in arr[1:]]
    C = [i[:2] + i[3:] for i in arr[1:]]
    D = [i[:3] + i[4:] for i in arr[1:]]
    E = [i[:-1] for i in arr[1:]]
    return arr[0][0] * four(A) - arr[0][1] * four(B) + arr[0][2] * four(C) - arr[0][3] * four(D) + arr[0][4] * four(E)

def six(arr):
    A = [i[1:] for i in arr[1:]]
    B = [i[:1] + i[2:] for i in arr[1:]]
    C = [i[:2] + i[3:] for i in arr[1:]]
    D = [i[:3] + i[4:] for i in arr[1:]]
    E = [i[:4] + i[5:] for i in arr[1:]]
    F = [i[:-1] for i in arr[1:]]
    return arr[0][0] * five(A) - arr[0][1] * five(B) + arr[0][2] * five(C) - arr[0][3] * five(D) + arr[0][4] * five(E) - arr[0][5] * five(F)


def seven(arr):
    A = [i[1:] for i in arr[1:]]
    B = [i[:1] + i[2:] for i in arr[1:]]
    C = [i[:2] + i[3:] for i in arr[1:]]
    D = [i[:3] + i[4:] for i in arr[1:]]
    E = [i[:4] + i[5:] for i in arr[1:]]
    F = [i[:5] + i[6:] for i in arr[1:]]
    H = [i[:-1] for i in arr[1:]]
    return arr[0][0] * six(A) - arr[0][1] * six(B) + arr[0][2] * six(C) - arr[0][3] * six(D) + arr[0][4] * six(E) - arr[0][5] * six(F) + arr[0][6] * six(H)


def eight(arr):
    A = [i[1:] for i in arr[1:]]
    B = [i[:1] + i[2:] for i in arr[1:]]
    C = [i[:2] + i[3:] for i in arr[1:]]
    D = [i[:3] + i[4:] for i in arr[1:]]
    E = [i[:4] + i[5:] for i in arr[1:]]
    F = [i[:5] + i[6:] for i in arr[1:]]
    H = [i[:6] + i[7:] for i in arr[1:]]
    I = [i[:-1] for i in arr[1:]]
    return arr[0][0] * seven(A) - arr[0][1] * seven(B) + arr[0][2] * seven(C) - arr[0][3] * seven(D) + arr[0][4] * seven(E) - arr[0][5] * seven(F) + arr[0][6] * seven(H) - arr[0][7] * seven(I)


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        result = binar(matrix)
    elif len(matrix) == 3:
        result = three(matrix)
    elif len(matrix) == 4:
        result = four(matrix)
    elif len(matrix) == 5:
        result = five(matrix)
    elif len(matrix) == 6:
        result = six(matrix)
    elif len(matrix) == 7:
        result = seven(matrix)
    else:
        result = eight(matrix)

    return result

if __name__ == '__main__':
    # arr = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
    # arr = [[1, 2, 3, 4],[5, 0, 2, 8],[3, 5, 6, 7],[2, 5, 3, 1]]

    arr = [[-4, 10, 2, 9, -7, 1, 4], [2, -5, 7, -8, 10, -5, -2], [-8, -4, 0, -1, 9, -5, 5], [7, -1, 6, -9, -1, 0, -9], [8, 1, -9, 6, -9, -5, 8], [7, -7, -7, -2, -8, -10, -1], [10, -2, 2, 7, 3, 4, -8]]
    print(determinant(arr))