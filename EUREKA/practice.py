from itertools import combinations

def solution(B, W):
    answer = 0

    Black = isWinner(B)
    White = isWinner(W)

    print(Black)
    print(White)

    if Black == White:
        answer = 0
    elif Black:
        answer = 1
    elif White:
        answer = -1
    

    return answer

def isWinner(target):
    for k in range(len(target), 5-1, -1):

        combi = list(combinations(target, k))

        for i in range(0, len(combi)):
            x = 0
            y = 0
            for j in range(0, 5):
                x += combi[i][j][0]
                y += combi[i][j][1]

            if (x%5==0) and (y%5 ==0) and (k==5):
                return True
    
    return False


    
    

# print(solution([[10,10],[11,10],[9,11],[11,11],[10,8],[12,13]], [[10,11],[9,10],[8,12],[11,12],[8,9],[7,8]]))
print(solution([[10,10],[10,11],[8,10],[9,10],[6,10],[11,10],[7,10]], [[9,11],[10,12],[11,13],[12,10],[5,10],[12,14]]))