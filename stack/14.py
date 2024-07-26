def solution(n, k, cmd):
    box = []
    temp = n

    for value in cmd:
        value_list = list(value.split(" "))

        if len(value_list) == 1:
            if value_list[0] == 'C':
                box.append(k)
                temp -= 1
                if temp == k:
                    k -= 1
                # 삭제된 위치의 바로 아래니까 앞으로 채워지니까 그대로인 것
            elif value_list[0] == 'Z':
                if box.pop() <= k:
                    k += 1
                temp += 1

        else:
            if value_list[0] == 'U':
                k -= int(value_list[1])
            elif value_list[0] == 'D':
                k += int(value_list[1])
    
    result = ["O"] * n

    for i in box:
        result[i] = "X"

    return "".join(result)

# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(8,2,cmd))