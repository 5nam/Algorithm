def solution(dirs):
    direction = list(dirs)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    x, y = 0, 0

    route = []
    
    # 방문한 좌표랑 방향 저장하기
    for value in direction:
        if value == 'U':
            nx, ny = x + dx[0], y + dy[0]
        elif value == 'D':
            nx, ny = x + dx[1], y + dy[1]
        elif value == 'R':
            nx, ny = x + dx[2], y + dy[2]
        elif value == 'L':
            nx, ny = x + dx[3], y + dy[3]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            px = x
            py = y
            x = nx
            y = ny
            if [px, x, py, y] not in route and [x, px, y, py] not in route:
                route.append([px, x, py, y])
        else:
            nx = x
            ny = y
    
    
    return len(route)