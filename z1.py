calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    up = string.upper()
    low = string.lower()
    res = (len(string), up, low)
    return res


def is_contains(string, list_to_search):
    flag = bool
    count_calls()
    string = string.lower()
    for i in list_to_search:
        i = i.lower()
        if string == i:
            flag = True
        else:
            flag = False
    return flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
