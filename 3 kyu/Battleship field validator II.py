# Ok
def validate_battlefield(battleField):
    s = 0
    for i in battleField:
        s += sum(i)
    if s != 20:
        return False
    if not search_four(battleField):
        return False
    if not search_three(battleField):
        return False
    if not search_two(battleField):
        return False
    return True


def search_four(matrix):
    ship = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                ship += 1
            else:
                ship = 0
            if ship == 4:
                matrix[i][j-3] = 4
                matrix[i][j - 2] = 4
                matrix[i][j - 1] = 4
                matrix[i][j] = 4
                return True

    for i in range(10):
        for j in range(10):
            if matrix[j][i] == 1:
                ship += 1
            else:
                ship = 0
            if ship == 4:
                matrix[j-3][i] = 4
                matrix[j-2][i] = 4
                matrix[j-1][i] = 4
                matrix[j][i] = 4
                return True
    return False


def search_three(matrix):
    ship = k = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                ship += 1
            else:
                ship = 0
            if ship == 3:
                k += 1
                ship = 0
                matrix[i][j - 2] = 3
                matrix[i][j - 1] = 3
                matrix[i][j] = 3
                if k == 2:
                    return True

    for i in range(10):
        for j in range(10):
            if matrix[j][i] == 1:
                ship += 1
            else:
                ship = 0
            if ship == 3:
                k += 1
                ship = 0
                matrix[j - 2][i] = 3
                matrix[j - 1][i] = 3
                matrix[j][i] = 3
                if k == 2:
                    return True
    return False

def search_two(matrix):
    ship = k = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                ship += 1
            else:
                ship = 0
            if ship == 2:
                k += 1
                ship = 0
                matrix[i][j - 1] = 2
                matrix[i][j] = 2
                if k == 3:
                    return True

    for i in range(10):
        for j in range(10):
            if matrix[j][i] == 1:
                ship += 1
            else:
                ship = 0
            if ship == 2:
                k += 1
                ship = 0
                matrix[j - 1][i] = 2
                matrix[j][i] = 2
                if k == 3:
                    return True
    return False


A = [
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
B = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# True should equal False
# C = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
# [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
# [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
# [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
# [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]]

C = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
]
# True should equal False


print(validate_battlefield(C))
# print(search_three(B))
# test(A)

# SOLUTION 1
def validateBattlefield(field):
    return battle(set([(r, c) for c in range(10) for r in range(10) if field[r][c]]), [1, 1, 1, 1, 2, 2, 2, 3, 3, 4])


def battle(grid, fleet):
    return sum(fleet) == len(grid) and (
                fleet == [] or any(battle(grid - p, fleet[:-1]) for p in possibles(grid, fleet[-1])))


def possibles(grid, ship):
    return [set(p) for p in
            [[(r + i, c) for i in range(ship)] for r, c in grid] + [[(r, c + i) for i in range(ship)] for r, c in grid]
            if set(p) <= grid]

# SOLUTION 2
