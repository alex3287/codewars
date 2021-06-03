from collections import deque


def prepare(s):
    result = s[0]
    for i in s[1:]:
        result += ' '+i
    return result


def to_postfix(infix):
    stack = deque()
    postfix = []
    infix = prepare(infix)
    power ={'(': 10, '-': 20, '+': 20, '*': 30, '/': 30, '^': 40}
    list_infix = infix.split()
    for j, i in enumerate(list_infix):
        if i in '0123456789':
            postfix.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            temp = stack.pop()
            while temp != '(':
                postfix.append(temp)
                temp = stack.pop()
        else:
            while len(stack) and power[stack[-1]] >= power[i]:
                if i == '^' and list_infix[j+1] in '0123456789(':
                    break
                postfix.append(stack.pop())
            stack.append(i)
    while len(stack):
        postfix.append(stack.pop())
    result = ''.join(postfix)
    return result


# s = "1^2^3"
# s = '0^4^7+4+0'  # '047^^4+0+'
# s = '(1+6-0)^4^8-(3-5+6/2-6)+8+(2*1+0*8/0)^4'  # 16+0-48^^35-62/+6--8+21*08*0/+4^+
s = '2+(3*5*3^8/0)*4^1^(7-2*7)-8^3'  # '235*38^*0/41727*-^^*+83^-'
print(prepare(s))
temp = prepare(s)
print(to_postfix(s))