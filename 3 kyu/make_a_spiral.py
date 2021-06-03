#Make a spiral
def check_column(A,i,j,t):
    if t < 0: m = -1
    else: m = 1

    if A[i+t][j] == 0 and A[i+t-m][j] == 0:
        if j == 0 or A[i+m][j-1] == 0 and A[i+m][j+1] == 0:
            return True
    return False

def check_row(A,i,j,t):
    if t < 0: m = -1
    else: m = 1

    if A[i][j+t] == 0 and A[i][j+t-m] == 0 and A[i-1][j+m] == 0 and A[i+1][j+m] == 0: #fix
        return True
    return False

def matrix(n):
    if n <2:
        return [[1]]
    if n == 2:
        return [[1,1],[0,1]]
    A=[[0]*n for i in range(n)]
    for i in range(n):
        A[0][i] = A[i][n-1] = A[n-1][i]= 1

    i = n-1
    j = 0
    t = 2
    flag = 1
    while flag:
        flag = 0
        while check_column(A,i,j,-t):
            i-=1
            A[i][j]=1
            flag = 1

        while check_row(A,i,j,t):
            j+=1
            A[i][j]=1
            flag = 1

        while j and check_column(A,i,j,t): #fix
            i+=1
            A[i][j]=1
            flag = 1

        while check_row(A,i,j,-t):
            j-=1
            A[i][j]=1
            flag = 1
    return A

if __name__ == "__main__":
    n=3
    print(matrix(n))
    for i in matrix(n):
        print(i)