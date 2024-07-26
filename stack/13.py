def solution(board, moves):
    box = []
    count = 0

    for value in moves:
        while board[value-1] and board[value-1][-1] == 0:
            board[value-1].pop()

        if box and board[value-1] and board[value-1][-1] == box[-1]:
            board[value-1].pop()
            box.pop()
            count += 2
        
        elif board[value-1]:
            box.append(board[value-1].pop())
    
    return count

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# board = [[],[1,3],[2,5,1],[4,2,4,4,2],[3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))