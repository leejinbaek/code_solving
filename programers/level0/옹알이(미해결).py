def solution(babbling):
    correct = ["aya","ye","woo","ma"]
    count = 0
    for word in babbling:
        temp_word = word
        for speak in correct:
            temp_word = temp_word.replace(speak,'')
        if temp_word == '':
            count += 1
    return count
# wooma의 경우는 유효하지만, womao의 경우는 유효하지 않은 값임
# 하지만 위와 같이 풀이하면 womao도 유효한 값으로 인식함 // 이에 정확히 일치하는 값으로 이루어져 있는지 판단하는 로직이 필요할 것으로 예상