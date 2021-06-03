def escape(carpark):
    result = []
    floors = len(carpark)-1
    for i, floor in enumerate(carpark):
        if 2 in floor:
            start = i
    point = find(carpark[start], 2)
    while start <= floors:
        index = find(carpark[start], 1)
        res = 0
        if index == -1:
            res = point - (len(carpark[start]) - 1)
            result = add(result, res)
        else:
            res = point - index
            result = add(result, res)
            if result[-1][0] =="D":
                result[-1] = "D"+ str(int(result[-1][1])+1)
            else:
                result.append('D1')
            point = index
        start += 1
    return result


def find(arr, number):
    index = -1
    for i, j in enumerate(arr):
        if j == number:
            index = i
            break
    return index


def add(arr, number):
    if number:
        if number < 0:
            arr.append('R'+str(abs(number)))
        else:
            arr.append('L'+str(number))
        return arr
    else:
        return arr

# carpark = [[1, 0, 0, 0, 2],
#            [0, 0, 0, 0, 0],
#            ]
# result = ["L4", "D1", "R4"]

carpark = [[1, 0, 0, 0, 2],
               [0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]
    # result = ["L4", "D1", "R4", "D1", "L4", "D1", "R4"]


print(escape(carpark))