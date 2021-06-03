def interleave(*args):
    result = []



    for i, j in zip(*args):
        result.append(i)
        result.append(j)
    return result

