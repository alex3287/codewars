def next_bigger(n):
    if n < 10:
        return -1
    N = [int(i) for i in str(n)]
    size = len(N)
    for i in range(size-2, -1, -1):
        if N[i] < max(N[i+1:]):
            return create_number(N, i)
    return -1

def create_number(N, i):
    number = N[i]
    left = N[:i]
    right = N[i+1:]
    right = change_number(number, right)
    new_number = ''.join([str(i) for i in (left + right)])
    return int(new_number)

def change_number(n, A):
    m = 10
    R = [n]
    for i in A:
        if n < i < m:
            if m < 10:
                R.append(m)
            m = i
        else:
            R.append(i)
    R = [m] + sorted(R)
    return R

print(next_bigger(144))


# top solution
import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

# top solution2

def next_bigger(n):
  n = str(n)[::-1]
  try:
    i = min(i+1 for i in range(len(n[:-1])) if n[i] > n[i+1])
    j = n[:i].index(min([a for a in n[:i] if a > n[i]]))
    return int(n[i+1::][::-1]+n[j]+''.join(sorted(n[j+1:i+1]+n[:j])))
  except:
    return -1

# top solution3
def next_bigger(n):
    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1
    a = n
    while True:
        a += 1
        if sorted(str(a)) == sorted(str(n)):
            return a