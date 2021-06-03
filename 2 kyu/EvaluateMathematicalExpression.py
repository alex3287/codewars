from collections import deque

def crash(string):
    for i, j in enumerate(string[:-2]):
        if j == '-' and string[i + 1] == ' ' and string[i - 1] == ' ' and (
                string[i - 2] not in '0123456789)' or string[i + 2] not in '0123456789/-+*('):
            return True
        elif j == '(' and string[i + 1] == '-' and string[i + 2] == ' ' and string[i + 3] != '(':
            return True
    if string[-1] == '-' or string[0] == '-' and string[1] == ' ' and string[2] in '-+*/':
        return True
    if string.strip() == '-':
        return True

    return False

def calc(string):
    if crash(string):
        return 'Invalid'
    stack = deque()
    s1 = infToPost(string)
    print(s1)
    for i in s1.split():
        if i == '/' or i == '+' or i == '-' or i == '*':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(math_operation(op1, i, op2))
        elif i == '^':
            op1 = stack.pop()
            stack.append(math_operation(op1, i))
        else:
            if '.' in i:
                stack.append(float(i))
            else:
                stack.append(int(i))
    return stack[0]

def coockString(string):
    s = ''
    for i in string:
        if i == ' ':
            continue
        if i in '()/-+*':
            s += ' ' + i + ' '
        elif ',' == i:
            s += '.'
        else:
            s += i
    temp = s.split()
    for i in range(len(temp)):
        if temp[i] == '-' and i == 0:
            temp[i] = '^'
        elif temp[i] == '-' and temp[i - 1] in '-+*/(':
            temp[i] = '^'
    s = ' '.join(temp)
    return s

def infToPost(string):
    preor = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    opstack = deque()
    result = []
    string = coockString(string)
    for j, i in enumerate(string.split()):
        if i == '(':
            opstack.append(i)
        elif i == ')':
            sing = opstack.pop()
            while sing != '(':
                result.append(sing)
                sing = opstack.pop()
        elif i in '-+*/^':
            while opstack and preor[opstack[-1]] >= preor[i]:
                result.append(opstack.pop())
            opstack.append(i)
        else:
            result.append(i)
    while opstack:
        result.append(opstack.pop())
    return ' '.join(result)

def math_operation(op1, sing, op2=0):
    if sing == '+':
        return op1 + op2
    if sing == '-':
        return op2 - op1
    if sing == '/':
        return op2 / op1
    if sing == '^':
        return -op1
    return op1 * op2


# print(calc('( 25 / -5 ) * 8 / 2'))
# print(calc('(24 * 0,5) * 8 / 2'))
# print(calc('8/16'))
# print(calc('8 + 1.5 - 1'))
# print(calc("(2 + (-2))*(2+3)"))
# print(calc('2 +1 - - 1'))    #  // Invalid
# print(calc('1- - 1 * 5'))     #  // Invalid
# print(calc('6 + - (4)'))  #  // Invalid
# print(calc('6 + -(- 4)')) #  // Invalid
# print(calc('0'))
# print(calc('1'))
# print(calc('- 34'))
# print(calc('123.45-(678.90 / (-2.5+ 11.5)-(((80 -(19.0)))+ 33.25)) / 20) - (123.45(678.90 / (-2.5+ 11.5)-(((80 -(19))) +33.25)) / 20) + (13 - 2)/ -(-11)'))
# print(calc('(4-4) - (-1 +2)'))
# print(calc("(2 -(-4 + 5))"))
print(calc("-7 * -(6 / 3)"))
print(calc("3 -(-1)"))
# print(calc("2 + -2"))
# print(calc("3 -(-1)"))
# print(calc('2 + -(-3+5 - -(-4+3))'))
# print(calc('-(-(-1))'))

# print(infToPost('41 (-54 - 92 * (-1 * 25))'))
# 41 -54 92 -1 25 * * - * 10 -61 53 - -30 / - -
