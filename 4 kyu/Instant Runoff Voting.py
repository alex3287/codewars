def drop(voters, A):
    mini = 10000000000000000
    for i in A:
        if A[i] < mini:
            mini = A[i]
            bad = i
    for i in voters:
        i.remove(bad)
    return voters


def runoff(voters):
    result = None
    maxi = 0
    A = {i:0 for i in voters[0]}
    for i in voters:
        for j in range(len(i)):
            if j == 0:
                A[i[j]] += 100
            else:
                A[i[j]] += 1
    B = [j for j in A.values()]

    if all(B[i] == B[i+1] for i in range(len(B)-1)):
        return None
    if B.count(max(B)) == 1:
        for i in A:
            if A[i] > maxi:
                maxi = A[i]
                result = i
    else:
        minus = drop(voters, A)
        return runoff(minus)
    return result if A[result] >= len(voters)*100 // 2 else None


# voters = [["dem", "ind", "rep"],
#                   ["rep", "ind", "dem"],
#                   ["ind", "dem", "rep"],
#                   ["ind", "rep", "dem"]]

# voters = [["a", "c", "d", "e", "b"],
#                  ["e", "b", "d", "c", "a"],
#                  ["d", "e", "c", "a", "b"],
#                  ["c", "e", "d", "b", "a"],
#                  ["b", "e", "a", "c", "d"]]

voters = [['Daisuke Aramaki', 'Drake Luft', 'Gihren Zabi', 'Brian J. Mason', 'Lex Luthor', 'Johan Liebert'],
          ['Daisuke Aramaki', 'Johan Liebert', 'Brian J. Mason', 'Drake Luft', 'Lex Luthor', 'Gihren Zabi'],
          ['Johan Liebert', 'Drake Luft', 'Brian J. Mason', 'Gihren Zabi', 'Lex Luthor', 'Daisuke Aramaki'],
          ['Lex Luthor', 'Johan Liebert', 'Brian J. Mason', 'Drake Luft', 'Gihren Zabi', 'Daisuke Aramaki'],
          ['Johan Liebert', 'Lex Luthor', 'Daisuke Aramaki', 'Gihren Zabi', 'Drake Luft', 'Brian J. Mason']]

# voters = [['Drake Luft', 'Abelt Dessler', 'Lex Luthor', 'Gihren Zabi'],
#           ['Abelt Dessler', 'Lex Luthor', 'Drake Luft', 'Gihren Zabi'],
#           ['Lex Luthor', 'Abelt Dessler', 'Drake Luft', 'Gihren Zabi'],
#           ['Lex Luthor', 'Drake Luft', 'Abelt Dessler', 'Gihren Zabi']]

# voters = [['Abelt Dessler', 'Johan Liebert', 'Drake Luft', 'Gihren Zabi', 'Lex Luthor'],
#           ['Gihren Zabi', 'Lex Luthor', 'Johan Liebert', 'Abelt Dessler', 'Drake Luft'],
#           ['Gihren Zabi', 'Drake Luft', 'Johan Liebert', 'Abelt Dessler', 'Lex Luthor'],
#           ['Drake Luft', 'Johan Liebert', 'Lex Luthor', 'Abelt Dessler', 'Gihren Zabi'],
#           ['Lex Luthor', 'Drake Luft', 'Gihren Zabi', 'Johan Liebert', 'Abelt Dessler'],
#           ['Abelt Dessler', 'Lex Luthor', 'Gihren Zabi', 'Johan Liebert', 'Drake Luft'],
#           ['Johan Liebert', 'Gihren Zabi', 'Abelt Dessler', 'Lex Luthor', 'Drake Luft'],
#           ['Drake Luft', 'Lex Luthor', 'Johan Liebert', 'Gihren Zabi', 'Abelt Dessler']]
print(runoff(voters))
D = runoff(voters)
# for i in D:
#     print(i)

# print(all( for j in range(len([i for i in D.values()]))))
