def whoIsNext(names, r):
    x=0
    t=2**x
    g=0
    while r > 5 * t:
        x+=1
        t=2**x
        g+=5*x
    if r % t != 0:
        r -= t-1
    number = r - g
    number %= 5
    return names[number]

if __name__  ==  "__main__":
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    print(whoIsNext(names, 5))
    