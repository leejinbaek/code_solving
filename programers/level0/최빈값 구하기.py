from collections import Counter

def solution(array):
        count = Counter(array) #Counter은 배열 값의 빈도수를 구해줌 dict형태로
        max_count = max(count.values())
        arr = [key for key, value in count.items() if max_count == value]
        if len(arr) > 1:
            return -1
        else:
            return arr[0]
