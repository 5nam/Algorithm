def solution(s):
    temp = s*2
    count = 0
    num = len(s)

    for i in range(num):
        s_list = list(temp[i:i+num])

        if(check_bracket(s_list)):
            count += 1
    
    return count

def check_bracket(s_list):
    stack = []

    for value in s_list:
        if value=='(' or value=='[' or value=='{':
            stack.append(value)

        elif value==')' or value==']' or value=='}':
            if not stack:
                return False
            stack.pop()

    return not stack

print(solution("[](){}"))