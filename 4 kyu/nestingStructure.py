def same_structure_as(original,other):
    if isinstance(original, type(other)):
        if len(original) != len(other):
            return False
        for i, j in zip(original, other):
            if type(i) != type(j):
                return False
            if isinstance(i, list) and (len(i) != len(j) or type(i[0]) != type(j[0])):
                return False
        A = [type(i) for i in original]
        B = [type(i) for i in other]
        while A and len(A) == len(B):
            temp = A.pop()
            if temp not in B:
                return False
            B.remove(temp)
        if len(A) == 0:
            return True
    if type(original) != type(other):
        return False
    return True

# top solution
def same_structure_as2(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as2(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)

print(same_structure_as2([1,'[',']'], ['[',']',1]))
print(same_structure_as2([1, [1, 1]], [[2, 2], 2]))