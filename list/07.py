def solution(dirs):
    
    dirs = list(dirs)
    location = {'U':(1, 0), 'D':(-1, 0), 'R':(0, 1), 'L':(0, -1)}
    x, y = 0, 0
    route = set()
    
    for dir in dirs:
        dx, dy = location[dir]
        nx, ny = x+dx, y+dy

        # 현재 상태에서 이미 다음 위치로 이동시킨 nx, ny 값이 5보다 작거나 같으면 현재 이동해도 되는 상태인 것
        if abs(nx) <= 5 and abs(ny) <= 5:
            route.add(x, y, nx, ny)
            route.add(dx, dy, x, y)

            x, y = nx, ny       
    
    return route // 2


# dirs = "ULURRDLLU"
dirs = "LULLLLLLU"
# dirs = "LLLLRRRRR"


print(solution(dirs))