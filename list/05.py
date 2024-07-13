# 행렬의 곱

def solution(arr1, arr2):
    
    # return [[sum(a * b for a, b in zip(arr1_row, arr2_col)) for arr1_row in arr1] for arr2_col in zip(*arr2)]
    return [[sum(a * b for a, b in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]