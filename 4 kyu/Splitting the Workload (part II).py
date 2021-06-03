def splitlist(lst):
    n = len(lst)
    if n == 1:
        return lst[0]
    lst.sort()
    A = []
    B = []
    if n % 2 == 0:
        flag = 0
        for i in range(0, n-1, 2):
            if lst[i] == lst[i+1]:
                A.append(lst[i])
                B.append(lst[i])
            elif sum(A) > sum(B):
                flag = 0
                A.append(min(lst[i], lst[i+1]))
                B.append(max(lst[i], lst[i+1]))
            else:
                flag = 1
                A.append(max(lst[i], lst[i + 1]))
                B.append(min(lst[i], lst[i + 1]))
    return abs(sum(A) - sum(B)), A, B, lst


A = [34, 76, 70, 13, 82, 59, 96, 4]
print(splitlist(A))