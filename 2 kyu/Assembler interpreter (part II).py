answer = ''
def assembler_interpreter(program):
    global answer
    result = dict()
    k = 0
    proga = [i.strip() for i in program.split('\n') if len(i.strip())>2]
    res = main(proga, result, k)
    return res


def main(proga, result, k):
    global answer
    lenght = len(proga)
    while k < lenght:
        action, *oper = proga[k].split()
        # реализация операций
        if action == 'mov':
            result = mov(result, oper[0], oper[1])
        elif action == 'inc':
            result[oper[0]] += 1
        elif action == 'dec':
            result[oper[0]] -= 1
        elif action == 'add':
            result = add(result, oper[0], oper[1])
        elif action == 'sub':
            result = sub(result, oper[0], oper[1])
        elif action == 'mul':
            result = mul(result, oper[0], oper[1])
        elif action == 'div':
            result = div(result, oper[0], oper[1])
        elif action == 'call':
            # result = call(result, oper[0], k, proga[k:])
            k = call(result, oper[0], k, proga)
        elif action == 'end':
            break
        elif action == 'ret':
            break
        elif action == 'msg':
            answer = msg(oper, result)
        elif action == 'cmp':
            flag = cmp(result, oper[0], oper[1])
        elif action == 'jne':
            if not flag:
                k = call(result, oper[0], k, proga)
        # print(k, '->', action, oper) fixme
        k += 1
    return answer


def cmp(result, first, second):
    f = first[:-1]
    s = second
    if f.isdigit():
        f = int(f)
    else:
        f = result[f]
    if s.isdigit():
        s = int(s)
    else:
        s = result[s]
    return f == s


def mov(result, a, b):
    a = a[:a.find(',')]
    if b.isdigit():
        result[a] = int(b)
    else:
        result[a] = result[b]
    return result


def add(result, a, b):
    a = a[:a.find(',')]
    if b.isdigit():
        result[a] += int(b)
    else:
        result[a] += result[b]
    return result


def sub(result, a, b):
    a = a[:a.find(',')]
    if b.isdigit():
        result[a] -= int(b)
    else:
        result[a] -= result[b]
    return result


def mul(result, a, b):
    a = a[:a.find(',')]
    if b.isdigit():
        result[a] *= int(b)
    else:
        result[a] *= result[b]
    return result


def div(result, a, b):
    a = a[:a.find(',')]
    if b.isdigit():
        result[a] //= int(b)
    else:
        result[a] //= result[b]
    return result


def call(result, name, k, proga):
    global answer
    old_k = k
    for i, j in enumerate(proga):
        if name+':' == j:
            main(proga, result, i+1)
            break
    return old_k


def msg(oper, result):
    answer = ''.join(oper)
    answer = answer.replace('\'', '')
    answer = answer.replace(',', ' ')
    finish = answer.find(';')
    if finish > 0:
        answer = answer[:finish]
    temp = answer.split(' ')
    for i in temp:
        if i in result:
            # answer = answer[1:answer.find(i)-2] + str(result[i])
            answer = answer.replace(i, str(result[i]))
            # answer = str(result[i]) + answer[1:answer.find(i)-2]  # TODO внес правки для второй лабы
    answer = answer.replace(' ', '')
    equel = answer.find('=')
    answer = answer[:equel] + ' = ' + answer[equel+1:]
    return answer


# тестирование программы
if __name__ == '__main__':
    program = '''
    ; My first program
    mov  a, 5
    inc  a
    call function
    msg  '(5+1)/2 = ', a    ; output message
    end
    
    function:
        div  a, 2
        ret
    '''

    # '(5+1)/2 = 3'

    program_factorial = '''
    mov   a, 5
    mov   b, a
    mov   c, a
    call  proc_fact
    call  print
    end
    
    proc_fact:
        dec   b
        mul   c, b
        cmp   b, 1
        jne   proc_fact
        ret
    
    print:
        msg   a, '! = ', c ; output text
        ret
    '''

    # '5! = 120'

    program2 = '''
    mov   a, 11           ; value1
    mov   b, 3            ; value2
    call  mod_func
    msg   'mod(', a, ', ', b, ') = ', d        ; output
    end

    ; Mod function
    mod_func:
        mov   c, a        ; temp1
        div   c, b
        mul   c, b
        mov   d, a        ; temp2
        sub   d, c
        ret
    '''

     # 'mod(11, 3) = 2')

    print(assembler_interpreter(program2))