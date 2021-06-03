def square2(A):
    for row in range(0,9,3):
        B = []
        for i in range(row, row+3):
            B += A[i][:3]
        if len(B) > len(set(B)):
            return False
        B = []
        for i in range(row, row+3):
            B += A[i][3:6]
        if len(B) > len(set(B)):
            return False
        B = []
        for i in range(row, row+3):
            B += A[i][6:9]
        if len(B) > len(set(B)):
            return False
    return True

def validSolution(board):
    for i in board:
        n = len(i)
        if len(set(i)) < n or 0 in i:
            return False
    for i in range(9):
        test = []
        for j in range(9):
            test.append(board[i][j])
        n = len(test)
        if len(set(test)) < n:
            return False
    return square2(board)

'''
сделано не мной 
def validSolution(board):
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)
    
вот еще
# PEP 8 - Function names should be in snake_case
def valid_solution(m):
    is_valid = lambda a: len(a) == 9 and all([i + 1 in a for i in range(9)])
    get_block_as_row = lambda n: [m[3 * (n / 3) + (i / 3)][(3 * n) % 9 + i % 3] for i in range(9)]
    return all([is_valid(r) for r in m]) and all([is_valid([r[i] for r in m]) for i in range(9)]) and all([is_valid(get_block_as_row(i)) for i in range(9)])

# Just to pass the Kata
validSolution = valid_solution

и еще
def validSolution(board):
    for x in range(9):
        arr = [board[y][x] for y in range(9)]
        arr2 = [board[x][y] for y in range(9)]
        arr3 = [board[i][y] for y in range(((x%3)*3),(((x%3)*3)+3)) for i in range((int(x/3)*3),(int(x/3)*3)+3)]
        for i in range(9):
            if arr[i] in arr[(i+1):]: return False
            if arr2[i] in arr2[(i+1):]: return False
            if arr3[i] in arr3[(i+1):]: return False
    return True
'''
