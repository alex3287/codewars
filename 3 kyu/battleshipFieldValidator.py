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


def validate_battlefield(field):
    s = 0
    for i in field:
        s += sum(i)
    if s != 20:
        return False
    if check_row_d(field):
        return False
    if max_ship_deap(field):
        return False
    if check_rul_ship(field):
        return False
    return True


#  top solution
def validateBattlefield(field):
    n, m = len(field), len(field[0])
    def cell(i, j):
        if i < 0 or j < 0 or i >= n or j >= m: return 0
        return field[i][j]
    def find(i, j):
        if cell(i + 1, j - 1) or cell(i + 1, j + 1): return 10086
        if cell(i, j + 1) and cell(i + 1, j): return 10086
        field[i][j] = 2
        if cell(i, j + 1): return find(i, j + 1) + 1
        if cell(i + 1, j): return find(i + 1, j) + 1
        return 1
    num = [0] * 5
    for i in xrange(n):
        for j in xrange(m):
            if cell(i, j) == 1:
                r = find(i, j)
                if r > 4: return False
                num[r] += 1
    [tmp, submarines, destroyers, cruisers, battleship] = num
    return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4