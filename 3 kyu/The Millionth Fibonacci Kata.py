# Ok
def mult(A):
    a00 = A[0][0]*0 + A[0][1]*1
    a01 = A[0][0]*1 + A[0][1]*1
    a10 = A[1][0]*0 + A[1][1]*1
    a11 = A[1][0]*1 + A[1][1]*1
    result = [[a00, a01], [a10, a11]]
    return result


def mult_matrix(n):
    A = [[0, 1], [1, 1]]
    for i in range(n-1):
        A = mult(A)
    return A


def fib(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return mult_matrix(n)[0][1]


def fib2(n):
     a = 1
     b = 1
     c = 1
     rc = 0
     d = 0
     rd = 1
     while n>0:
         if n%2!=0:
             tc = rc
             rc = rc*a + rd*c
             rd = tc*b + rd*d
         ta = a
         tb = b
         tc = c
         a = a*a  + b*c
         b = ta*b + b*d
         c = c*ta + d*c
         d = tc*tb+ d*d
         n //= 2
     return rc

if __name__ == '__main__':
    print(fib2(9))