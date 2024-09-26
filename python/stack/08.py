def solution(str):
    data = list(str)
    stack = []

    for item in data:
        if item == '(':
            stack.append(item)
        elif item == ')':
            if not stack: # 스택이 비었다면
                return False
            else:
                stack.pop()
        
    return len(stack) == 0