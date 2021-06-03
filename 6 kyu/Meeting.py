def crash(s):
    result = [i.split(':') for i in s.split(';')]
    result = ['('+i[1].upper() +', '+ i[0].upper()+')' for i in result]
    result.sort()
    return ''.join(result)


s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

print(crash(s))