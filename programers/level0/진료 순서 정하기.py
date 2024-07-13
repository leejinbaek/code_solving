def solution(emergency):
    #방법 1: 각 리스트의 요소를 서로 비교하여 가장 큰 값부터 array의[0]번째,
    #       그 다음 [1]번째 이런식으로 출력하는 방법
        
    # array = ["1","2","3","4","5","6","7","8","9","10"] #array[0~9]
    # for i in range(len(emergency)):
    #     if emergency[i] > emergency[i+1]:
            
    #방법 2: 새롭게 정렬된 배열을 만들고 그 배열에 해당되는 순서를 dict으로 만들어 출력하는 방법
    enumerate_emergency = sorted([(e,i) for i,e in enumerate(emergency)], reverse=True)
    answer = [0]*len(emergency)
    for order, (e,i) in enumerate(enumerate_emergency, start=1):
        answer[i] = order
    return answer