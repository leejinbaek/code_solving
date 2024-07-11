def solution(my_string):
    vowel = ["a","e","i","o","u"]
    new = ""
    for char in my_string:
        if char not in vowel:
            new += char
    return new

# def solution(my_string):
#     return "".join([i for i in my_string if not(i in "aeiou")])

def ll(mds):
    return "".join([i for i in mds if i not in "aeiou"])