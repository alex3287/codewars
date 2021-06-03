def longest(s):
    lenght = len(s)
    if lenght < 2:
        return s
    result = ''
    temp = s[0]
    maxi = 0
    k = 1
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            temp += s[i+1]
            k += 1
            if k > maxi:
                maxi = k
                result = temp
        else:
            k = 1
            if k > maxi:
                maxi = k
                result = temp
            temp = s[i+1] if i+2 < lenght and s[i+1] <= s[i+2] else ''
    return result


# s = 'asdfaaaabbbbcttavvfffffdf' # 'aaaabbbbctt')
s = 'zyba' # 'aaaabbbbctt')
print(longest(s))