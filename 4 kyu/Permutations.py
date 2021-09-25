def pig_it(text):
    A = text.split()
    b = ''
    for i in A:
        if i in ',.!?':
            b += i
        else:
            c = i[1:]+i[0]+'ay'
            b += c + ' '
    return b, len(text), len(b)


def pig_it2(text):
    a = text.split(' ')
    b = ''
    for i in a:
        if i in '?.,!':
            b += i
        else:
            c = i[1:] + i[0] + 'ay'
            b += c + ' '
    return b, 'ads'

s = 'Pig latin is cool !'
print(pig_it2(s))