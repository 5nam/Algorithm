# 모의고사

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = [0, 0, 0]

    first_answer = []
    second_answer = []
    third_answer = []

    # 답지 생성
    first_answer += list(first * (len(answers) // len(first)))
    first_answer += list(first[:(len(answers) % len(first))])
    second_answer += list(second * (len(answers) // len(second)))
    second_answer += list(second[:(len(answers) % len(second))])
    third_answer += list(third * (len(answers) // len(third)))
    third_answer += list(third[:(len(answers) % len(third))])
    
    # 답지 비교
    for i in range(len(answers)):
        if answers[i] == first_answer[i]:
            count[0] += 1
        if answers[i] == second_answer[i]:
            count[1] += 1
        if answers[i] == third_answer[i]:
            count[2] += 1
    
    value = max(count)
    answer = []
    
    if value == count[0]:
        answer.append(1)
    if value == count[1]:
        answer.append(2)
    if value == count[2]:
        answer.append(3)
        
    return answer

print(solution(list([1,2,3,4,5])))