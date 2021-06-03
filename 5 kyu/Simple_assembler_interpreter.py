def simple_assembler(program):
    # A = [i for i in program.split('\n')]
    A = program
    answer = dict()
    size = len(A)
    k = 0
    while k < size:
        if A[k][:3] == 'mov':
            _, var, num = A[k].split()
            if num.isalpha():
                answer[var] = answer[num]
            else:
                answer[var] = int(num)
        elif A[k][:3] == 'inc':
            _, var = A[k].split()
            answer[var] += 1
        elif A[k][:3] == 'dec':
            _, var = A[k].split()
            answer[var] -= 1
        elif A[k][:3] == 'jnz':
            _, var, num = A[k].split()
            if var.isalpha():
                if answer[var] != 0:
                    k += int(num)
                    continue
            elif var != '0':
                k += int(num)
                continue
        k += 1
    return answer


code1 = ['mov a -10','mov b a','inc a','dec b','jnz a -2']

code1 = ['mov a 1', 'mov b 1', 'mov c 0', 'mov d 26', 'jnz c 2', 'jnz 1 5', 'mov c 7', 'inc d', 'dec c', 'jnz c -2', 'mov c a', 'inc a', 'dec b', 'jnz b -2', 'mov b c', 'dec d', 'jnz d -6', 'mov c 18', 'mov d 11', 'inc a', 'dec d', 'jnz d -2', 'dec c', 'jnz c -5']



print(simple_assembler(code1))


# best code

# def simple_assembler(program):
#     d, i = {}, 0
#     while i < len(program):
#         cmd, r, v = (program[i] + ' 0').split()[:3]
#         if cmd == 'inc': d[r] += 1
#         if cmd == 'dec': d[r] -= 1
#         if cmd == 'mov': d[r] = d[v] if v in d else int(v)
#         if cmd == 'jnz' and (d[r] if r in d else int(r)): i += int(v) - 1
#         i += 1
#     return d


# def simple_assembler(program):
#     regs = {}
#     def get(x):
#         return int(regs.get(x, x))
#     i = 0
#     while i < len(program):
#         op, x, y, *_ = program[i].split() + [None]
#         i += 1
#         if op == 'mov':   regs[x] = get(y)
#         elif op == 'inc': regs[x] += 1
#         elif op == 'dec': regs[x] -= 1
#         elif get(x):      i += get(y) - 1
#     return regs