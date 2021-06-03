def num_list(string):
    arr = string.split()
    result = 0
    if len(arr) == 1:
        if '-' in arr:
            pass
        else:
            return D[arr[0]]
    for i in range(len(arr)):
        if '-' in arr[i]:
            a,b = arr[i].split('-')
            arr.insert(i,b)
            arr.insert(i,a)
            arr.pop()
    return arr

def parse_int(string):
    arr = num_list(string)
    print(string)
    D1 = {'zero': '0','one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
         'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10',
        'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14',
         'fifteen': '15', 'sixteen': '16', 'seventeen': '17', 'eighteen': '18',
         'nineteen': '19',
        'twenty': '20', }
    result = ''
#     for i in arr:
#         result += D[i]
#    return result
    return ''

D = {'zero': '0','one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
         'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10',
        'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14',
         'fifteen': '15', 'sixteen': '16', 'seventeen': '17', 'eighteen': '18',
         'nineteen': '19',
        'twenty': '20', }

print(num_list('fifteen'))