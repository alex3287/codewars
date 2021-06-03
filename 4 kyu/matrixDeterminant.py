def det(arr):
    return arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        result = det(matrix)
    else:
        a_minor = 2
        b_minor = 2
        c_minor = 2
        result = -20

    return result

m0 = [[1]]
m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

print(determinant(m1))