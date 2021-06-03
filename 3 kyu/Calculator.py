from collections import deque


class Calculator(object):

    def evaluate(self, string):
        stack = deque()
        s1 = self.infToPost(string)
        for i in s1.split():
            if i == '/' or i == '+' or i == '-' or i == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(self.math_operation(op1, op2, i))
            else:
                stack.append(float(i))
        return stack[0]

    def coockString(self, string):
        s = ''
        for i in string:
            if '(' in i:
                s += i[0] + ' ' + i[1:]
            elif ')' in i:
                s += i[:-1] + ' ' + i[-1]
            else:
                s += i
        return s

    def infToPost(self, string):
        preor = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
        opstack = deque()
        result = []
        string = self.coockString(string)
        for i in string.split():
            if i == '(':
                opstack.append(i)
            elif i == ')':
                sing = opstack.pop()
                while sing != '(':
                    result.append(sing)
                    sing = opstack.pop()
            elif i == '+' or i == '-' or i == '*' or i == '/':
                while opstack and preor[opstack[-1]] >= preor[i]:
                    result.append(opstack.pop())
                opstack.append(i)
            else:
                result.append(i)

        while opstack:
            result.append(opstack.pop())

        return ' '.join(result)

    def math_operation(self, op1, op2, sing):
        if sing == '+':
            return op1 + op2
        if sing == '-':
            return op2 - op1
        if sing == '/':
            return op2 / op1
        return op1 * op2



# print(infToPost('( 25 + 4 ) * 8 / 2'))
# print(calc('( 25 + 4) * 8 / 2'))

# print(coockString('(25 + 4) * 8 / 2'))

print(Calculator().evaluate("2 / 2 + 1.1 * 4 - 6"))