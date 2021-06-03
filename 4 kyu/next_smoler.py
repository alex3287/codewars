def swap(dig,B):
    if min(B) == B[-1]:
        return dig, B
    dig, B[B.index(min(B))] = B[B.index(min(B))], dig
    return dig, B

def swap2(dig,B):
    m=dig
    flag = 0
    for i in B:
        if i > dig and i < max(B) and i > m:
            m = i
            flag = 1
    if flag:
        B.remove(m)
        B.append(dig)
        dig = m
    return dig, B

def swap3(buf,B):
    m = B[-1]
    temp = buf
    for i in B:
        if buf < i and i < m:
            buf = i
    if buf != temp:
        B.remove(buf)
        B.append(temp)
    return buf, B

def check(digit,A):
    for i in A:
        if digit > i and i != '0':
            return False
    return True

def next_smaller(n):
    if n < 21:
        return -1
    if (20 < n < 100):
        if (n%10 == 0) or (n%10 > n // 10) or (n%10 == n // 10):
            return -1
        return n%10 * 10 + n//10
    A = list(str(n))
    B=[A[-1]]
    A=A[:-1]
    while A:
        if A[-1] > min(B) and not(len(A)==1 and check(A[-1],B)):
            buf = min(B)
            B.remove(min(B))
            B+=A[-1]
            A=A[:-1]
            break
        B.append(A[-1])
        A=A[:-1]
    else:
        return -1
    
    if buf =='0':
        buf, B = swap(buf,B)
    if B[-1] == max(B):
        buf, B = swap2(buf,B)
    #fix
    elif B[-1] < max(B[:-1]):
        buf, B = swap3(buf,B)
    
    B.sort(reverse=1)
    res = ('').join(A)+buf+('').join(B)
    result = int(res)
    return result 


if __name__ == '__main__':
    next_smaller(513)


# вот тут код крутого чувака
'''
def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]: i -= 1
    if i <= 0: return -1
    while s[j] >= s[i - 1]: j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0': return -1
    return int(''.join(s))
'''