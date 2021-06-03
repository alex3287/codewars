def my_sort(s):
    m = set(s.strip().lower())
    string = sorted(m)
    string = ''.join(string)
    return string


def find_uniq(arr):
    D = {}
    for i in arr:
        t = my_sort(i)
        D.setdefault(t,0)
        D[t] += 1

    for j,k in D.items():
        if k==1:
            find=j
            break
    for word in arr:
        if find == my_sort(word):
            find = word
            break
    return find

if __name__ == "__main__":
    s = ['aSdfA ','rty','aasdf','asdf']
    print(find_uniq(s))