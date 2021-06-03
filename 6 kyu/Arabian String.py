def camelize(str_):
    str_ = str_.lower()
    str = ''
    for i in str_:
        if i.isalnum():
            str += i
        else:
            str += ' '
    str = ''.join([i.capitalize() for i in str.split()])
    return str


s = 'Rugby:Club:2013'
print(camelize(s))