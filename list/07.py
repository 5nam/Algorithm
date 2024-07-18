def solution(dirs):
    route = set()
    direction = {'U':(0, 1), 'D':(0, -1),'R':(1, 0), 'L':(-1, 0)}

    x, y = 0, 0

    for value in dirs:
        nx, ny = x + direction[value][0], y + direction[value][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            route.add((x, y, nx, ny))
            route.add((nx, ny, x, y))
            x, y = nx, ny

    return len(route)//2
