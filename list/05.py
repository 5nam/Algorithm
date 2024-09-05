def solution(arr1, arr2):
    
    rows = len(arr1) #2 
    cols = len(arr2[0]) #2
    value_num = len(arr2)

    print(rows)
    print(cols)
    
    answer = []

    for _ in range(rows):
        temp = []
        for _ in range(cols):
            temp.append(0)

        answer.append(temp)

    print(answer)


    arr2 = list(zip(*arr2))
    
    for i1 in range(rows):
        for i2 in range(cols):
            for i3 in range(value_num):
                answer[i1][i2] += arr1[i1][i3] * arr2[i2][i3]
    
    return answer

# arr1 = [[2,3,2], [4,2,4], [3,1,4]]
# arr2 = [[5,4,3], [2,4,1], [3,1,1]]

# arr1 = [[1,4], [3,2], [4,1]]
# arr2 = [[3,3], [3,3]]

arr1 = [[1, 2, 2], [3, 2, 3]]
arr2 = [[1,2], [3,4], [5,6]]

print(solution(arr1, arr2))