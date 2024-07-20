def solution(value):
    stack = []
    
    while(value != 1):
        remainder = value % 2
        value //= 2

        stack.append(remainder)

    stack.append(value)

    result = ""
    for _ in range(len(stack)):
        result += str(stack.pop())
    
    return result

print(solution(12345))