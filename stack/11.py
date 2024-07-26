def solution(S):
    s_list = list(S)
    stack = [s_list[0]]

    for value in s_list:
        if stack and stack[-1] == value:
            stack.pop()

        else:
            stack.append(value)
    
    if stack:
        return 0
    
    return 1

print(solution("baabaa"))