def solution(n):
    array =[]
    while n > 0:
        if n%2 != 0:
            array.append(n)
        n -= 1
    return sorted(array)

# return [i for i in range(1,n+1) if i%2 != 0]