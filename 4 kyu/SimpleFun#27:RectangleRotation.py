def rectangle_rotation(a, b):
    result = a-1
    result += (result*(b/2))+((result-1)*(b/2))
    return result
    # S1 = a*b/2/2
    # S2 = a/2*b/2
    # return 2*(S1+S2)


print(rectangle_rotation(8, 6))
# rectangle_rotation(6,4),23)
# rectangle_rotation(30,2),65)
# rectangle_rotation(8,6),49)
# rectangle_rotation(16,20),333)