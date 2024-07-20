def solution(value):
    stack = []
    
    while(value != 1):
        remainder = value % 2
        value //= 2

        stack.append(remainder)

    stack.append(value)

    result = ""
    while stack:
        result += str(stack.pop())
    
    return result