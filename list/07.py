def solution(dirs):
    direction = list(dirs)
    coordinate = [0,0,0]
    route = []
    n = len(direction)
    
    # 방문한 좌표랑 방향 저장하기
    for i in range(n):
        if coordinate[1] < 5 and direction[i] == 'U':
            coordinate[1] += 1
            coordinate[2] = 0
        elif coordinate[1] > -5 and direction[i] == 'D':
            coordinate[1] -= 1
            coordinate[2] = 1
        elif coordinate[0] < 5 and direction[i] == 'R':
            coordinate[0] += 1
            coordinate[2] = 2
        elif coordinate[0] > -5 and direction[i] == 'L':
            coordinate[0] -= 1
            coordinate[2] = 3
        
        # 이렇게 짠 이유는 파이썬은 리스트를 append 하면, 그 리스트의 주소값을 저장하기 때문에
        # 하나의 리스트를 계속 이용해서 연산할 경우 값이 같이 변하므로!
        route.append([coordinate[0], coordinate[1], coordinate[2]])
    
    # route 중복 제거 및 개수 반환
    unique_set = set(map(tuple, route))
    
    return len(unique_set)

print(solution("LULLLLLLU"))