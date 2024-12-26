
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
    temp = sorted(target, key = lambda x : x[0])

    for i in range(0, len(temp)):
        result = top(target, temp[i]) or topRight(target, temp[i]) or right(target, temp[i]) or bottomRight(target, temp[i]) or bottom(target, temp[i])

        if(result):
            break

    return result
    

def top(target, temp):
    cnt = 1
    num = 1
    while [temp[0]-num, temp[1]] in target:
        cnt += 1
        num += 1
    
    if cnt == 5 and [temp[0]+1, temp[1]] not in target:
        return True
    
    return False

def topRight(target, temp):
    cnt = 1
    num = 1
    while [temp[0]-num, temp[1]+num] in target:
        cnt += 1
        num += 1
    
    if cnt == 5 and [temp[0]+1, temp[1]-1] not in target:
        return True
    
    return False

def right(target, temp):
    cnt = 1
    num = 1
    while [temp[0], temp[1]+num] in target:
        cnt += 1
        num += 1
    
    if cnt == 5 and [temp[0], temp[1]-1] not in target:
        return True
    
    return False

def bottomRight(target, temp):
    cnt = 1
    num = 1

    while [temp[0]+num, temp[1]+num] in target:
        cnt += 1
        num += 1
    
    if cnt == 5 and [temp[0]-1, temp[1]-1] not in target:
        return True
    
    return False

def bottom(target, temp):
    cnt = 1
    num = 1

    while [temp[0]+num, temp[1]] in target:
        cnt += 1
        num += 1
    
    if cnt == 5 and [temp[0]-1, temp[1]] not in target:
        return True
    
    return False

print(solution([[10,10],[11,10],[9,11],[11,11],[10,8],[12,13]], [[10,11],[9,10],[8,12],[11,12],[8,9],[7,8]]))
print(solution([[10,10],[10,11],[8,10],[9,10],[6,10],[11,10],[7,10]], [[9,11],[10,12],[11,13],[12,10],[5,10],[12,14]]))