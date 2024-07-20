def solution(str):
    data = list(str)
    stack = []

    for item in data:
        if item == '(':
            stack.append(item)
        elif item == ')':
            stack.pop()
        
    return len(stack) == 0