def solution(board, moves):
    box = []
    count = 0
    n = len(board[0])
    transpose = []

    # 행렬 바꿈
    for i in range(n):
        temp = []
        for j in range(-1, -n-1, -1):
            if board[j][i] != 0: # 0 값 제거
                temp.append(board[j][i])
        transpose.append(temp)

    for value in moves:

        if box and transpose[value-1] and transpose[value-1][-1] == box[-1]:
            transpose[value-1].pop()
            box.pop()
            count += 2
        
        elif transpose[value-1]:
            box.append(transpose[value-1].pop())
    
    return count

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
board = [[1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [1, 0, 0, 0, 0], [3, 0, 0, 0, 0]]

moves = [1,1,1,1]
print(solution(board, moves))