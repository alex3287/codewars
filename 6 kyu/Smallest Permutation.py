def min_permutation(n):
    if n == 0:
        return 0
    s = str(n)
    sing = ''
    if s[0] == '-':
        sing = s[0]
        s = s[1:]
    result = list(s)
    result.sort()
    if result[0] == '0':
        i = 0
        while result[i] == '0':
            i += 1
        result[0], result[i] = result[i], result[0]
    result = ''.join(result)
    if sing:
        result = sing+result
    result = int(result)
    return result


print(min_permutation(-20010210))