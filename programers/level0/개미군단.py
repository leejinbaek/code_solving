def solution(hp):
    nhp = hp%5
    nnhp = nhp%3
    return hp//5 + nhp//3 + nnhp