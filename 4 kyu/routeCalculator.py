from collections import deque

def check(expression):
    for i in expression:
        if i not in '0123456789.-+*$':
            return False
    return True


def coock_string(expression):
    result = ''
    for i in expression:
        if i in '-+*$':
            result += ' ' + i + ' '
        else:
            result += i
    return result


def prefix(expression):
    preo = {'-': 1, '+': 1, '*': 2, '$': 2}
    stack = deque()
    result = []
    for i in expression.split():
        if i in '-+*$':
            while stack and preo[stack[-1]] >= preo[i]:
                result.append(stack.pop())
            stack.append(i)
        else:
            result.append(i)
    while stack:
        result.append(stack.pop())
    return ' '.join(result)


def operation(op1, op2, sing):
    if sing == '+':
        return op1 + op2
    elif sing == '-':
        return op1 - op2
    elif sing == '$':
        return op1 / op2
    return op1 * op2

def calculate(expression):
    if check(expression):
        string = coock_string(expression)
        prefix_string = prefix(string)
        stack = deque()
        for i in prefix_string.split():
            if i in '-+*%':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(operation(op1, op2, i))
            else:
                if '.' in i:
                    stack.append(float(i))
                else:
                    stack.append(int(i))
        return stack[0]
    return "400: Bad request"

# print(calculate('3x+1'))
print(calculate("10+5"))


# top solution
import re

ADDSUB, MULDIV = '+-', '*$'

def calculate(expression):
    return "400: Bad request" if re.search(r'[^+*$\d.-]', expression) else parseAndEval(expression, ADDSUB)

def parseAndEval(expression, ops):
    v = 0
    for op,part in re.findall(r'([{0}])?([^{0}]+)'.format(ops), expression):
        if not op:    v  = float(part) if ops == MULDIV else parseAndEval(part, MULDIV)
        elif op=='*': v *= float(part)
        elif op=='$': v /= float(part)
        elif op=='+': v += parseAndEval(part, MULDIV)
        elif op=='-': v -= parseAndEval(part, MULDIV)
    return v