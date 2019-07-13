def match(item,lst):
    if item in lst:
        return True
    return False

lst=[1,2,3,4,5,6,7,8,9,10]

print(match(11,lst))