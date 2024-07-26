def solution(prices):
    p_num = len(prices)
    stack = [0]
    result = [0] * p_num

    for i in range(1, p_num):
        if prices[stack[-1]] > prices[i]:
            while stack and prices[stack[-1]] > prices[i]:
                result[stack.pop()] = i - stack[-1]
        stack.append(i)
    
    s_num = len(stack)

    for i in range(s_num):
        result[stack.pop()] = p_num - 1 - stack[-1]

    return result

print(solution([1,2,3,2,3]))