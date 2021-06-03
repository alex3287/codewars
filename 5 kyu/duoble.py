def whoIsNext(names, r):
    x=0
    t=2**x
    low = 1
    while r > low * 2 + 3:
        x+=1
        t=2**x
        low = low * 2 + 4 
    position = 0
    while True:
        low += t
        if r < low:
            break
        position += 1
    return names[position]


if __name__  ==  "__main__":
    #names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    #print(whoIsNext(names, 7230702951))
    x=0
    t=2**x
    k = 1
    for i in range(35):
        k = k * 2 + 4
        x+=1
        t=2**x
        
        print(k, '-->',k * 2 + 3, '==', t)
        if 7230702951 < k:
            break
    