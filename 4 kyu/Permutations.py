from itertools import *


# stuff = [1, 2, 3]
# for L in range(0, len(stuff)+1):
#     for subset in itertools.combinations(stuff, L):
#         print(subset)

def permutations(string):
    # A = list(string)
    # B = []
    # for L in range(3, len(A) + 1):
    #     for subset in combinations(A, L):
    #         B.append(subset)
    # A = [i for i in combinations(string, 3)]
    B = [i for i in product(string, string, string, string)]
    return B


s = 'aabb'
print(permutations(s))
# ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']