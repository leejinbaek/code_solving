def solution(my_string):
    new_string = ''
    for i in my_string:
        if i.isupper():
            new_string += i.lower()
        elif i.islower():
            new_string += i.upper()
        else:
            new_string += i
    return new_string