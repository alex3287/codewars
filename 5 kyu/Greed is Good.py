# Ok
def score(dice):
    x1 = x2 = x3 = x4 = x5 = x6 = 0
    x1 = dice.count(1)
    x2 = dice.count(2)
    x3 = dice.count(3)
    x4 = dice.count(4)
    x5 = dice.count(5)
    x6 = dice.count(6)
    result = 0
    if x1 >= 3:
        result += 1000
        x1 -= 3
    if x1 == 2:
        result += 100
        x1 -= 1
    if x1 == 1:
        result += 100
    if x5 >= 3:
        result += 500
        x1 -= 3
    if x1 == 2:
        result += 50
        x1 -= 1
    if x1 == 1:
        result += 50
    if x2 >= 3:
        result += 200
    elif x3 >= 3:
        result += 300
    elif x4 >= 3:
        result += 400
    elif x6 >= 3:
        result += 600
    return result


print(score([4, 4, 4, 3, 3]))