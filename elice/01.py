num = '364'
num_list = list(num)

def solution(num, num_list):
    if(len(num_list) == 1) : 
        return num 
    elif (len(num_list) == 2) :
        num_list.reverse()
        num2 = strListToInt(num_list)
        
        if(int(num) >= num2) :
            return num
        else :
            return num2
    
    for _ in range(-1, -len(num_list)-1, -1):
        num_list = recursion(-2, -1, num_list)
    
    
    result = strListToInt(num_list)

    return result
    

def recursion(left_index, right_index, num_list):
    if(len(num_list)*(-1) > left_index):
        return num_list
    if(int(num_list[left_index]) < int(num_list[right_index])):
        if(strListToInt(num_list) > strListToInt(num)):
            return num_list
        temp = num_list[left_index]
        num_list[left_index] = num_list[right_index]
        num_list[right_index] = temp
        return num_list

    elif(int(num_list[left_index]) >= int(num_list[right_index])):
        if(strListToInt(num_list) > strListToInt(num)):
            temp_list = list(num_list)
            temp = num_list[left_index]
            num_list[left_index] = num_list[right_index]
            num_list[right_index] = temp
            if((int(num) < strListToInt(temp_list) and int(num) >= strListToInt(num_list)) and strListToInt(temp_list) < strListToInt(num_list)):
                num_list = temp_list
                return num_list
        
        recursion(left_index-1, right_index-1, num_list)
        return num_list

    recursion(left_index-1, right_index, num_list)
    return num_list

def strListToInt(num_list):
    num_list = ''.join(num_list)
    return int(num_list)
    
    

print(solution(num, num_list))
