from collections import deque

def longest_palindrome(s):
    if s == '':
        return ''
    if s == s[::-1]:
        return s
    if len(s) == 1:
        return s
    result = s[0]
    dack = deque(s)
    while len(dack) > 1:
        left = dack.popleft()
        right = dack.pop()

    return result
