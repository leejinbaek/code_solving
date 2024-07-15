def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        else:
            return 4
    elif dot[0] < 0:
        if dot[1]  > 0:
            return 2
        else:
            return 3

## 가독성++
def solution(dot):
    x, y = dot
    if x > 0:
        return 1 if y > 0 else 4
    else:
        return 2 if y > 0 else 3
