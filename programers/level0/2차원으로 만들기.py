def solution(num_list, n):
    array =[]
    for i in range(0,len(num_list),n):
        array.append(num_list[i:i+n])
    return array