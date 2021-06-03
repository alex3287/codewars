def hex_string_to_RGB(hex_string):
    D = dict()
    r, g, b = hex_string[1:3], hex_string[3:5], hex_string[5:]
    D['r'] = int(r, 16)
    D['g'] = int(g, 16)
    D['b'] = int(b, 16)
    return D


s = "#FF9933"
print(hex_string_to_RGB(s))
# {'r':255, 'g':153, 'b':51})
# ("#beaded"), {'r':190, 'g':173, 'b':237})
# ("#000000"), {'r':0, 'g':0, 'b':0})
# ("#111111"), {'r':17, 'g':17, 'b':17})
# ("#Fa3456"), {'r':250, 'g':52, 'b':86})