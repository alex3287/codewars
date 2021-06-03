def simple_assembler(program):
    result = dict()
    for j, i in enumerate(program):
        temp = i.split()
        if temp[0] == 'mov':
            if temp[2].isdigit():
                result[temp[1]] = int(temp[2])
            else:
                result[temp[1]] = result[temp[2]]
        elif temp[0] == 'inc':
            result[temp[1]] += 1
        elif temp[0] == 'dec':
            result[temp[1]] -= 1
        elif temp[0] == 'jnz':
            if int(temp[2]) < 0:
                n = temp[1]
                start = j + int(temp[2])
                finish = j
                while result[n]:
                    for j, i in enumerate(program[start:finish]):
                        temp2 = i.split()
                        if temp2[0] == 'mov':
                            if temp2[2].isdigit():
                                result[temp2[1]] = int(temp[2])
                            else:
                                result[temp2[1]] = result[temp[2]]
                        elif temp2[0] == 'inc':
                            result[temp2[1]] += 1
                        elif temp2[0] == 'dec':
                            result[temp2[1]] -= 1
    return result

def culc(program):
    global result
    for j, i in enumerate(program):
        temp = i.split()
        if temp[0] == 'mov':
            if temp[2].isdigit():
                result[temp[1]] = int(temp[2])
            else:
                result[temp[1]] = result[temp[2]]
        elif temp[0] == 'inc':
            result[temp[1]] += 1
        elif temp[0] == 'dec':
            result[temp[1]] -= 1
    return result

# print(culc(['mov a 5','inc a']))
# print(simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a']))
print(simple_assembler(['mov c 12', 'mov b 0', 'mov a 200', 'dec a', 'inc b', 'jnz a -2',
'dec c', 'mov a b', 'jnz c -5', 'jnz 0 1', 'mov c a']))
# simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a'])
#
# ''' visualized:
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a
# ''''