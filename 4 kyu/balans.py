def balanced_parens(n):
    if n < 1:
        return [""]
    s1 = '('
    s2 = ')'
    A=[]
    for i in range(n*2):
        if i % 2 == 0:
            s1[i]

            s3 = 7
            if s3 not in A:
                A.append(s3)


    return A

if __name__ == '__main__':
    print(balanced_parens(3))