def solution(my_string, letter):
    array = ''
    for i in my_string:
        if i != letter:
            array += i
    return array

    #replace 메서드 사용 가능
    ## return my_string.replace(letter,'')