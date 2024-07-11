def solution(num_list):
    even = 0
    odd = 0
    for num in num_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]

# def solution(num_list):
#     answer = [0,0]
#     for n in num_list:
#         answer[n%2]+=1
#     return answer