def krazy_king_blackjack (hand, king_value):
    A = 0
    K = 0
    s = 0
    for i in hand:
        if i in 'JQ':
            s += 10
        elif i == 'A':
            A += 1
        elif i == 'K':
            K += 1
        else:
            s += int(i)
    if K * 10 + s < 21 and K * king_value + s + A * 11 != 21:
        s += 10 * K
    else:
        s += king_value * K
    for i in range(A):
        if s + 11 < 22 and A - i < 2:
            s += 11
        else:
            s += 1
    # if s > 21:
    #     return False
    return s

print(krazy_king_blackjack(['A', 'A', 'A', 'K', '4'], 9))
print(krazy_king_blackjack(['K', 'A', '3'], 7))