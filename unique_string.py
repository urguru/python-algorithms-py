def unique_string(str):
    str = str.replace(' ', '')
    storage = set()
    for letter in str:
        if letter in storage:
            return False
        else:
            storage.add(letter)
    return True


print(unique_string('abcde'))


def unique_string2(str):
    str = str.replace(' ', '')
    return len(set(str)) == len(str)


print(unique_string2('abcde'))
