def solve_runes(runes):
    exmple, equel = runes.split('=')
    if '?' not in exmple:
        result = str(eval(exmple))
        n = 0
        st = equel
        while result != st and n < 10:
            st = change(equel, n)
            n += 1
        return n-1 if n < 10 else -1
    n = 0
    n_1, n_2 = exmple.split('*')
    while n < 10:
        st = change(equel, n)
        if '?' in n_1:
            num_1 = change(n_1, n)
        else:
            num_1 = n_1
        if '?' in n_2:
            num_2 = change(n_2, n)
        else:
            num_2 = n_2
        test = str(eval(num_1 + ' * ' + num_2))
        if test == st:
            return n
        n += 1
    # return n - 1 if n < 10 else -1
    return exmple, equel


def change(st, n):
    new = ''
    for i in st:
        if i == '?':
            new += str(n)
        else:
            new += i
    return new


if __name__ == '__main__':
    print(solve_runes("1+1=?"))
    print(solve_runes("123*45?=5?088"))  # 6