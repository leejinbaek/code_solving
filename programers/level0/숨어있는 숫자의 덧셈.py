def solution(my_string):
    count = 0
    for i in my_string:
        if i in "123456789":
            count += int(i)
    return count

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())