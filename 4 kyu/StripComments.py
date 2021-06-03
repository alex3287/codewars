def solution(string, markers):
    for i in markers:
        index = string.find(i)
        while index > -1:
            string = slice_string(string, index)
            index = string.find(i)
    return string


def slice_string(string, index):
    start = index
    finish = len(string)
    for i in range(start, len(string)):
        if string[i] == '\n':
            finish = i
            break
    string = string[:start-1] + string[finish:]
    return string

# s = "apples, pears # and bananas\ngrapes\nbananas !apples"
# m = ["#", "!"]
# "apples, pears\ngrapes\nbananas")

# s = "a #b\nc\nd $e f g"
# m = ["#", "$"]
# "a\nc\nd")

s = "apples, pears # and bananas\ngrapes\nbananas !#apples"
m = ['#', '!']

print(solution(s, m))

# s = string.index(markers[1])
# for i in markers:
#     string += string[:string[string.index(i)]]
# s = string[:string.index(markers[0])] + string[string.index('\n'):string.index(markers[1])]