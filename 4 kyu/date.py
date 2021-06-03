def translate(seconds):
    y = seconds // 31536000
    d = seconds % 31536000 // 86400
    h = seconds % 31536000 % 86400 // 3600
    m = seconds % 31536000 % 86400 % 3600 // 60
    s = seconds % 31536000 % 86400 % 3600 % 60 % 60
    return y,d,h,m,s

def writes(K):
    y, d, h, m, s = K
    if y:
        if y > 1:
            y = str(y) +' years'
        else:
            y =str(y) + ' year'
    else: y = ''

    if d:
        if d > 1:
            d = str(d) +' days'
        else:
            d =str(d) + ' day'
    else: d = ''

    if h:
        if h > 1:
            h = str(h) +' hours'
        else:
            h =str(h) + ' hour'
    else: h = ''

    if m:
        if m > 1:
            m = str(m) +' minutes'
        else:
            m =str(m) + ' minute'
    else: m = ''

    if s:
        if s > 1:
            s = str(s) +' seconds'
        else:
            s =str(s) + ' second'
    else: s = ''
    A = [i for i in (y, d, h, m, s) if i]
    return A

def format_duration(seconds):
    if seconds ==0:
        return 'now'
    A = writes(translate(seconds))
    if len(A) == 1:
        return A[0]
    if 'second' in A[-1] or 'minute' in A[-1]:
        A[-1] = ' and '+A[-1]
        result = (', ').join(A[:-1]) + A[-1]
    else:
        result = (', ').join(A)
    return result




if __name__ == '__main__':
    n = 3600 * 24 * 365 * 5 + 86400 + 3600*8 + 60
    print(n)

    # 86400
    # 31536000