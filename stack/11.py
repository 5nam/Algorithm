def solution(S):
    s_list = list(S)
    stack = [s_list[0]]
    n = len(s_list)

    for i in range(1, n):
        if stack and stack[-1] == s_list[i]:
            stack.pop()

        else:
            stack.append(s_list[i])
    
    if stack:
        return 0
    
    return 1

print(solution("baabaa"))