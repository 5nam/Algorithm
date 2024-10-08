def solution(value):
    stack = []
    
    while(value != 1):
        remainder = value % 2
        value //= 2

        stack.append(remainder)

    stack.append(value)

    stack.reverse()
        
    return ''.join(map(str, stack))

print(solution(10))