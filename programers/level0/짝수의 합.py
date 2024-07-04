def solution(n):
    # 제너레이터 표현식
    return sum(i for i in range(2, n+1, 2))