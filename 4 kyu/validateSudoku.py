class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        n = len(self.data)
        sqrt = n**0.5
        if int(sqrt) < sqrt:
            return False
        for i in self.data:
            if len(i) != n or 0 in i or n+1 in i:
                return False
        for row in self.data:
            if any(type(i) != int for i in row):
                return False
        if n > 3 and self.check_litl():
            return False
        return True

    def check_litl(self):
        n = len(self.data)
        sq = int(n**0.5)
        h = sum(range(n+1))
        A = {i: [] for i in range(sq)}
        for i in range(n):
            if i % sq == 0:
                if A[0]:
                    for k in A.values():
                        t = sum([sum(i) for i in k])
                        if t != h:
                            return True
                A = {i: [] for i in range(sq)}
            for j in range(sq):
                A[j] += [self.data[i][j*sq:(j+1)*sq]]
        for k in A.values():
            if sum([sum(i) for i in k]) != sum(range(n+1)):
                return True
        return False






test = Sudoku([ [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [2, 3, 1, 5, 6, 4, 8, 9, 7],
                [3, 1, 2, 6, 4, 5, 9, 7, 8],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [5, 6, 4, 8, 9, 7, 2, 3, 1],
                [6, 4, 5, 9, 7, 8, 3, 1, 2],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [8, 9, 7, 2, 3, 1, 5, 6, 4],
                [9, 7, 8, 3, 1, 2, 6, 4, 5]])

# print(test.is_valid())

test2 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],

  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])
print(test2.is_valid())