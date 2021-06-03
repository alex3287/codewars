from collections import deque

def encode_rail_fence_cipher(string, n):
    if len(string) % 2*n != 0:
        k_chars = n+(n - len(string) % n)
        string += '='*k_chars
        print(string)
    step = (n-1)*2
    s = string[::step]
    for i in range(n-2, 0, -1):
        jump = i*2
        k = 0
        start = k * step + (n - i - 1)
        temp = ''
        right = jump + start
        while len(string) > right:
            temp += string[start] + string[start + jump]
            k += 1
            start = k * step + (n - i - 1)
            right += step
        s += temp
    s += string[step//2::step]
    correct_s =''
    for i in s:
        if i != '=':
            correct_s += i
    return correct_s

def decode_rail_fence_cipher(string, n):
    row = (len(string)-1) // (n-1)
    Words = []
    first_slice = row // 2 + 1
    first = string[:first_slice]
    string = string[first_slice:]
    if row % 2 == 0:
        last_slice = -(first_slice-1)
    else:
        last_slice = -(first_slice)
    last = string[last_slice:]
    string = string[:last_slice]
    if n == 2:
        result = ''
        while first:
            result += first[0]
            first = first[1:]
            if last:
                result += last[0]
                last = last[1:]
        return result
    Words.append(first)
    step_1 = len(string) // (n-2)
    step_2 = len(string) % (n-2)
    if step_2 == 0 and (n-1)*row+1 != len(string):
        step_2 = n-2

    if row % 2 != 0:
        for i in range(n-2-step_2):
            Words.append(string[:row])
            string = string[row:]
        for j in range(step_2):
            Words.append(string[:row+1])
            string = string[row+1:]
    else:
        for i in range(step_2):
            Words.append(string[:row+1])
            string = string[row+1:]
        for j in range(n-2-step_2):
            Words.append(string[:row])
            string = string[row:]
    Words.append(last)

    if len(Words[0]) == len(Words[-1]):
        Words[0] = Words[0]+'='
    template = max(len(Words[-2]), len(Words[1]))
    repeat = len(last)*2
    if step_2 > 0 and row % 2 == 0:
        repeat+=1
    for i in range(1, n-1):
        if len(Words[i]) != template:
            Words[i] += '='
    result = ''
    for i in range(repeat):
        if i % 2 == 0:
            for j in range(n):
                if Words[j]:
                    result += Words[j][0]
                    Words[j] = Words[j][1:]
        else:
            Temp = Words[1:-1]
            Temp.reverse()
            if len(Temp[0]) < 1:
                continue
            for k in range(n-2):
                result += Temp[k][0]
                Temp[k] = Temp[k][1:]
            Temp.reverse()
            Words = [Words[0]] + Temp + [Words[-1]]
    if Words[0]:
        result += Words[0]
    correct_result = ''
    for i in result:
        if i != '=':
            correct_result += i
    return correct_result


# TODO так раньше было
# def decode_rail_fence_cipher(string, n):
#     print(string, n)
#     if len(string) < n:
#         return string
#     g = len(string) // (n*2-1) + 2
#     begin = deque(list(string[:g]))
#     end = deque(list(string[len(string)-g+1:]))
#     new_string = string[g:len(string)-g+1]
#     A = []
#     step = len(new_string) // (n-2)
#     for i in range(n-2):
#         A.append(deque(list(new_string[i*step:(i+1)*step])))
#     temp = []
#     for i in range(g-1):
#         temp.append(begin.popleft())
#         #  down
#         for j in A:
#             temp.append(j.popleft())
#
#         temp.append(end.popleft())
#
#         #  up
#         for k in range(n-3, -1, -1):
#             temp.append(A[k].popleft())
#     temp.append(begin.popleft())
#
#     result = ''.join(temp)
#     return result


if __name__ == '__main__':
    test_4 = 'eejrs i  pcoermAupvP  de sr u a!esaiastip,tef!q axo lt itia  o pitece sdudn,tD ai vt c nioVanoo oii.msei iert  earri!utatasn sakgmmmseu n reoim mritte omlnuiepntd ieecve qrnesp eieafafusmnsn uu iibiiis r tixio ae sti dirui eufatutercr'
    # print(encode_rail_fence_cipher(test_4, 9))
    print(decode_rail_fence_cipher(test_4, 10))

    # 'empentmqb irraoc,Aeuteotinieieta  epjvfsostssu penid!Pr qui   rf eos.d  sdanmamitaielks,xe  otegnaxtifumiD sirl  miaou femiat  u iespuatesner i  atvtutm esnd  ti!pea  n strini ec sca  are  cdueernoioa irocuirr viiopsetiV!meiu ii  uatiraueeloer '  +
    # 'eritau  iibqmtnepmeA,coarri initoetujpe  ateiesstsosfvrP!dinep ur   iuq s  d.soe ftimamnad ex,skleiaxangeto is Dimufitoaim  lr  taimef uaupsei u  i renset mtutvtap!it  dnsets n  aecs ce inir  era  aoionreeudciucori aespoiiv rruiem!Vit'

