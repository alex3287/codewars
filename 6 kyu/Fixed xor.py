def fixed_xor(a, b):
    if a and b:
        if len(b) != len(a):
            if len(b) > len(a):
                a, b = b, a
            new_len = len(b)
            a = a[:new_len]

        result = hex(int(a, 16) ^ int(b, 16))[2:]
        new_len = len(b)
        if len(result) < new_len:
            result = '0'* (new_len-len(result)) + result
        return a, b, result
    return ""


# xor("785a6677b3e52f0e7", "a8d97da7441"), "d0831bd0f7f")
a = "785a6677b3e52f0e7"
b = "a8d97da7441"
print(fixed_xor(a, b))