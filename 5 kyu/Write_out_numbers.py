NUMBERS = \
    {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
     19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
     50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def les_100(n):
    if n < 21 or (n % 10 == 0 and n < 91):
        return NUMBERS[n]
    d, e = n // 10 * 10, n % 10
    return NUMBERS[d] + '-' + NUMBERS[e]


def les_1000(n):
    return NUMBERS[n] + ' hundred'


def number2words(n):
    """ works for numbers between 0 and 999999 """
    ed = s = t = dt = st = 0
    result = ''
    if n < 100:
        return les_100(n)
    elif n < 1000:
        s, ed = n // 100, n % 100
        result = les_1000(s)
        if ed:
            result += ' ' + les_100(ed)
    elif n < 100000:
        dt, s, ed = n // 1000, n % 1000 // 100, n % 100
        result = les_100(dt) + ' thousand'
        if s:
            result += ' ' + les_1000(s)
        if ed:
            result += ' ' + les_100(ed)
    else:
        st, dt, s, ed = n // 100000, n % 100000 // 1000, n % 1000 // 100, n % 100
        result = les_1000(st) + ' thousand'
        if dt:
            result = les_1000(st) + ' ' + les_100(dt) + ' thousand'
        if s:
            result += ' ' + les_1000(s)
        if ed:
            result += ' ' + les_100(ed)
    return result


# лучшее решение
# d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
# 6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
# 11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
# 16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
# 20:'twenty',30:'thirty',40:'forty',50:'fifty',
# 60:'sixty',70:'seventy',80:'eighty',90:'ninety',
# 100:'hundred',1000:'thousand'}
# def number2words(n):
#     """ works for numbers between 0 and 999999 """
#     if 0<=n<=20:return d[n]
#     if 20<n<=99 and n%10:return d[10*(n//10)]+'-'+d[n%10]
#     if 20<n<99:return d[10*(n//10)]
#     if n<1000 and n%100==0:return d[n//100]+' '+d[100]
#     if 100<n<=999:return d[n//100]+' '+d[100]+' '+number2words(n%100)
#     if n%1000==0:return d[n//1000]+' '+d[1000]
#     return number2words(n//1000)+' '+d[1000]+' '+number2words(n%1000)