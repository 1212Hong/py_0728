# Q7 Answer Template

def solution(s):
    answer = []
    
    answer.append(s[0])
    
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            answer.append(s[i])
    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)