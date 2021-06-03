def bonus_time(salary, bonus):
    if bonus:
        salary *= 10
    s = '$' + str(salary)
    return s


print(bonus_time(10000, True))


# (bonus_time(10000, True), '$100000')
# (bonus_time(25000, True), '$250000')
# (bonus_time(10000, False), '$10000')
# test.assert_equals(bonus_time(60000, False), '$60000')
# test.assert_equals(bonus_time(2, True), '$20')
# test.assert_equals(bonus_time(78, False), '$78')
# test.assert_equals(bonus_time(67890, True), '$678900')
