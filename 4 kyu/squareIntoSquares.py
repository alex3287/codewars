# def find(A, num):
#     l = 0
#     r = len(A)-1
#     x = A[(r+l)//2]
#     while x != num and r > l:
#         if x > num:
#             r = (r+l) // 2 - 1
#         else:
#             l = (r+l) // 2 + 1
#         x = A[(r + l) // 2]
#     if num < x:
#         x = A[l-1]
#     return x
#
#
# def decompose(n):
#     A = [i*i for i in range(1, n)]
#     new_n = n*n
#     result = []
#     i = -1
#     x = A[i]
#     while new_n > 0 and len(A) > (n-1) // 2:
#         result = [int(x**0.5)] + result
#         new_n -= x
#         if new_n:
#             x = find(A, new_n)
#             if int(x**0.5) in result:
#                 result.clear()
#                 new_n = n*n
#                 A = A[:len(A) - 1]
#                 i = -1
#                 x = A[i]
#     if new_n:
#         return None
#     else:
#         return result
def find(A, num):
    l = 0
    r = len(A)-1
    x = A[(r+l)//2]
    while x != num and r > l:
        if x > num:
            r = (r+l) // 2 - 1
        else:
            l = (r+l) // 2 + 1
        x = A[(r + l) // 2]
    if num < x:
        x = A[l-1]
    return x


def decompose(n):
    arrSquare = [i*i for i in range(1, n)]
    arrNumbers = [i for i in range(1, n)]
    square = n*n
    result = []
    i = -1
    x = arrSquare[i]
    while square > 0:
        result.insert(0, arrNumbers[i])
        square -= x
        if square > 0:
            x = find(arrSquare, square)
            if arrNumbers[arrSquare.index(x)] in result:
                result.clear()
                new_n = n*n
                A = A[:len(A) - 1]
                i = -1
                x = A[i]
    # if new_n:
    #     return None
    # else:
    #     return result
    return result

# print(decompose(10000000))

print(decompose(50)) # [1, 2, 3, 7, 9]
# A = [i*i for i in range(2, 10, 2)]
# print(A)
# print(find(A, 25))