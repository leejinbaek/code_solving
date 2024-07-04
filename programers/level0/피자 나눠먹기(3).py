def solution(slice, n):
    if slice/n < 1:
        if n%slice != 0:
            return n//slice + 1
        else:
            return n//slice
    else:
        return 1