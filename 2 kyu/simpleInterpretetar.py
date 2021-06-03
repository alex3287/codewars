import re
from collections import deque


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


class Interpreter:
    VARIABLES = {}

    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        tokens = tokenize(expression)
        if not tokens:
            return ''
        if '=' in tokens:
            i = tokens.index('=')
            var, example = tokens[0], tokens[i + 1:]
            postfix = self.infToPost(example)
            self.VARIABLES[var] = str(self.calc(postfix))
        else:
            if len(expression.split()) == 2:
                print("ERROR: Invalid input. " + ' '.join(tokens))
                return
            postfix = self.infToPost(tokens)
        return self.calc(postfix)

    def calc(self, string):
        stack = deque()
        for i in string.split():
            if i.isalpha():
                if i in self.VARIABLES:
                    i = self.VARIABLES[i]
                else:
                    print('ERROR: Invalid identifier. No variable with name ' + i + ' was found.')
            if i in '/%+-*':
                op1 = stack.pop()
                op2 = stack.pop()
                if type(op1) == str or type(op2) == str:
                    stack.append(0)
                else:
                    stack.append(self.math_operation(op1, op2, i))
            else:
                if '.' in i:
                    stack.append(float(i))
                else:
                    stack.append(int(i))
        return stack[0]

    def infToPost(self, array):
        preor = {'*': 3, '/': 3, '%': 3, '+': 2, '-': 2, '(': 1}
        opstack = deque()
        result = []
        for j, i in enumerate(array):
            if i == '(':
                opstack.append(i)
            elif i == ')':
                sing = opstack.pop()
                while sing != '(':
                    result.append(sing)
                    sing = opstack.pop()
            elif i in '+-*/%':
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
        if sing == '%':
            return op2 % op1
        return op1 * op2


interpreter = Interpreter()
# print(interpreter.input("x= 2 + 5"))
# print(interpreter.input("y = x + 5"))
print(interpreter.input('2+3'))
print(interpreter.input('1 2'))


# top solution

from ast import parse, Expr, Assign, BinOp, Name, Num
from operator import add, sub, mul, mod, truediv


class Interpreter:

    def __init__(self):
        self.vars = {}

    def input(self, expression):

        op = {'Sub': sub, 'Add': add, 'Mult': mul, 'Div': truediv, 'Mod': mod}

        def _eval(node):

            if isinstance(node, Expr):
                return _eval(node.value)
            if isinstance(node, Name):
                return self.vars[node.id]
            if isinstance(node, Num):
                return node.n
            if isinstance(node, BinOp):
                return op[type(node.op).__name__](_eval(node.left), _eval(node.right))
            if isinstance(node, Assign):
                name = node.targets[0].id
                self.vars[name] = _eval(node.value)
                return self.vars[name]

        tree = parse(expression)
        return _eval(tree.body[0]) if len(tree.body) else ''
