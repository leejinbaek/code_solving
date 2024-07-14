#for 문을 이용하는 방법
def solution(cipher, code):
    return "".join([cipher[i] for i in range(code-1, len(cipher), code)])

#슬라이싱 사용 방법
def solution(cipher, code):
    return cipher[code-1::code]