def crash_string(s1,s2):
    D1 = {}
    D2 = {}
    for i in s1:
        if i.isalpha() and i == i.lower():
            D1.setdefault(i,0)
            D1[i]+=1
    for i in s2:
        if i.isalpha() and i == i.lower():
            D2.setdefault(i,0)
            D2[i]+=1
    return D1, D2

def filter(D1,D2):
    D={}
    for i in D1.keys():
        if i in D2 and max(D1[i],D2[i]) > 1:
            if D1[i] > D2[i]:
                D[i+'1'] = D1[i]
            elif D2[i] > D1[i]:
                D[i + '2'] = D2[i]
            else:
                D[i + '='] = D2[i]
    for j in D1.keys():
         if j+'=' not in D and j+'1' not in D and j+'2' not in D and D1[j] > 1:
            D[j + '1'] = D1[j]
    for k in D2.keys():
        if k+'=' not in D and k+'1' not in D and k+'2' not in D and D2[k] > 1:
            D[k + '2'] = D2[k]
    return D

def collect(D):
    A=[]
    for i, j in D.items():
        s = ''
        s=i[1]+':'+i[0]*j
        A.append(s)
    A.sort()
    return A

def my_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if len(A[j][2:]) > len(A[j-1][2:]) or \
                    (len(A[j][2:]) == len(A[j-1][2:]) and A[j][0] < A[j-1][0]): #fix
                A[j-1], A[j] = A[j], A[j-1]
    return A

def mix(s1, s2):
    D1, D2 = crash_string(s1,s2)
    D = filter(D1,D2)
    A = collect(D)
    A = my_sort(A)
    s ='/'.join(A)
    return s

if __name__ == '__main__':
    a, b = "Are they here", "yes, they are here"
    #a, b = " In many languages", " there's a pair of functions"
    f, g = crash_string(a, b)
    print(f,'\n',g)
    print(filter(f,g))
    print(collect(filter(f,g)))
    print(mix(a, b))
#"1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
#"2:eeeee/2:yy/=:hh/=:rr"