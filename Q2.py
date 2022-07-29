def solution(numbers):
    answer = 45
    for i in range(len(numbers)):
        answer -= numbers[i]
    return answer

numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
print(answer)
