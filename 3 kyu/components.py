S3 = '''\
+--+--+--+
|     |  |
+  +--+--+
|     |  |
+--+--+--+'''
S = '''\
+--+--+--+
|  |     |
+  +--+--+
|  |  |  |
+--+--+--+'''

S2 = '''\
+--+--+--+
|  |     |
+  +--+  +
|  |  |  |
+--+--+--+
|  |  |  |
+--+--+--+'''
def rows_and_columns(grid):
    all_plus = columns = 0
    for i,j in enumerate(grid):
        if j == '+':
            all_plus += 1
        elif j == '\n' and columns == 0:
            columns = all_plus
    rows = all_plus / columns
    return int(rows - 1), columns - 1

def cell(grid):
    roof = columns = rows = 0
    W = []
    F = []
    for i,j in enumerate(grid):
        if j == '-':
            floor += 1
        elif j == '|':
            columns += 1
        elif j == '\n':
            if roof == 0:
                roof = floor
            elif grid[i-1] == '|':
                W.append(columns-1)
                columns = 0
            elif grid[i-1] == '+':
                F.append(floor//2)
            floor = 0
    F.append(roof//2)
    return W, F

def test(grid):
    F = list(grid.split('\n'))
    F = F[1:-1]
    F2 = list(i[1:-1] for i in F)
    Col = []
    Row = []
    for j, i in enumerate(F2,1):
        if j % 2 == 1:
            col = i.count('|') + 1
            Col.append(col)
        else:
            row = i.count('--')
            Row.append(row)
    return F2, Col, Row

def components(grid):
    width, height, wall, floor = data(grid)
    if wall == floor:
        return [(1, wall)]

if __name__ == '__main__':
    #print(rows_and_columns(S))
    #print(cell(S))
    print(test(S))
    #for i,j in enumerate(S2):
   #     print(i,j)


