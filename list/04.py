# 모의고사

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = [0, 0, 0]

    
    # 답지 비교
    for index, value in enumerate(answers):
        if answers[index] == first[index % len(first)]:
            count[0] += 1
        if answers[index] == second[index % len(second)]:
            count[1] += 1
        if answers[index] == third[index % len(third)]:
            count[2] += 1
    
    value = max(count)
    answer = []
    
    for index in range(3):
        if value == count[index]:
            answer.append(index+1)
        
    return answer

print(solution(list([1,2,3,4,5])))