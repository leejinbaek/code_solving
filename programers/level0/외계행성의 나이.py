def solution(age):
    # 인덱스를 이용해서 출력하는 방법 구상
    array = ["a","b","c","d","e","f","g","h","i","j"] #0~9까지의 수
    age_str = [int(i) for i in str(age)] #age_str = [?, ?]
    result = ''
    for i in age_str:
        result += array[i]
    return result

#아스키 코드를 이용해서 나이를 출력하는 방식
def solution(age):
    return ''.join([chr(int(i) + 97) for i in str(age)])