def solution(my_string, n):
    # join을 이용하는 방법도 존재
    
    # result = 'x'.join(i*n for i in my_string)
    # print(result)

    result = ''
    for string in my_string:
        result += string*n
    return result
