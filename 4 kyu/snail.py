def snail(snail_map):
    if snail_map[0]:
        A = []
        while snail_map:
            A += snail_map[0]
            del snail_map[0]
            if snail_map:
                for i in snail_map:
                    A.append(i.pop())
                A += snail_map[-1][::-1]
                del snail_map[-1]
            if snail_map:
                for i in snail_map[::-1]:
                    A.append(i[0])
                    del i[0]
        return A
    return []


#  top solution
def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a

#  second top solution
def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
