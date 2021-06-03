def check_row_d(field):
    for i in range(9):
        for j in range(1, 9):
            if field[i][j] == 1 and field[i+1][j-1] == 1 or field[i][j] == 1 and field[i+1][j+1]:
                return True
    return False

def max_ship_deap(field):
    ships = {1: 4, 2: 3, 3: 2, 4: 1}
    for j in range(10):
        lenght = 0
        for i in range(10):
            if j == 0 and field[i][j] and field[i][j+1] == 0:
                lenght += 1
            elif j == 9 and field[i][j] and field[i][j-1] == 0:
                lenght += 1
            elif 0 < j < 9:
                if (field[i][j] and field[i][j+1] == 0) and (field[i][j] and field[i][j-1] == 0):
                    lenght += 1
            if lenght and field[i][j] == 0 or lenght and i == 9:
                if lenght > 4:
                    return True
                if ships[lenght] == 0:
                    return True
                else:
                    ships[lenght] -= 1
                    lenght = 0
    return False


def check_rul_ship(field):
    for j in range(9):
        for i in range(1, 9):
            if (field[i][j] and field[i+1][j]) and (field[i][j+1] or field[i+1][j+1]):
                return True
    return False


def validate_battlefield(battleField):
    s = 0
    for i in battleField:
        s += sum(i)
    if s != 20:
        return False
    # if check_row_d(battleField):
    #     return False
    # if max_ship_deap(field):
    #     return False
    # if check_rul_ship(battleField):
    #     return False
    return True

A = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(A))