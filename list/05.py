# 행렬의 곱

def solution(arr1, arr2):
    rows = len(arr1)
    cols = len(arr2[0])

    answer = [[0] * cols for _ in range(rows)]

    arr1_rows = len(arr1)
    arr2_cols = len(arr2[0])
    arr1_cols = len(arr1[0])

    for i in range(arr1_rows):
        for j in range(arr2_cols):
            value = 0
            for k in range(arr1_cols):
                value += arr1[i][k] * arr2[k][j]

            answer[i][j] = value

    return answer