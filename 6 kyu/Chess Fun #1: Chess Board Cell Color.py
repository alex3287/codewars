# Ok
def chess_board_cell_color(cell1, cell2):
    R1 = 'ACEG'
    R2 = 'BDFH'
    l1, n1 = cell1[0], cell1[1]
    l2, n2 = cell2[0], cell2[1]
    if (l1 in R1 and l2 in R1) or (l1 in R2 and l2 in R2):
        if n1 % 2 == 0 and n2 % 2 == 0 or n1 % 2 == 1 and n2 % 2 == 1:
            return True
        return False
    if n1 % 2 == 0 and n2 % 2 == 1 or n1 % 2 == 1 and n2 % 2 == 0:
        return True
    return False

print(chess_board_cell_color('A2','B3'))
