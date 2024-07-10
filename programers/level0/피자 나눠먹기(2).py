def solution(n):
    #6조각 , 나머지 x
    #최소공배수 구하기
    def gcd(a,n):
        while n:
            a,n = n, a%n
        return a
    least = 6*n // gcd(6,n)
    return least//6 
    