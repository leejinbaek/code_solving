def solution(n, k):
    bill = n*12000 + k*2000
    if n>=10:
        bill -= n//10*2000
    return bill

# def solution(n, k):
#     return 12000 * n + 2000 * (k - n // 10)