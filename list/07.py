def solution(dirs):
    
    dirs = list(dirs)
    now = [0, 0]
    route = []
    count = 0
    
    for dir in dirs:
        if dir == 'U':
            if now[1] == 5:
                continue

            next_now = [now[0], now[1] + 1]
            new_route = [now, next_now]
            new_route_reverse = [next_now, now]
            
            now = next_now

        elif dir == 'D':
            if now[1] == -5:
                continue
            
            next_now = [now[0], now[1] - 1]
            new_route = [now, next_now]
            new_route_reverse = [next_now, now]
            
            now = next_now
        elif dir == 'R':
            if now[0] == 5:
                continue
            
            next_now = [now[0] + 1, now[1]]
            new_route = [now, next_now]
            new_route_reverse = [next_now, now]
            
            now = next_now
            
        elif dir == 'L':
            if now[0] == -5:
                continue

            next_now = [now[0] - 1, now[1]]
            new_route = [now, next_now]
            new_route_reverse = [next_now, now]
            
            now = next_now
        
        if new_route not in route or new_route_reverse not in route:
            count += 1
            route.append(new_route)
            route.append(new_route_reverse)
            
    
    return count


# dirs = "ULURRDLLU"
dirs = "LULLLLLLU"
# dirs = "LLLLRRRRR"


print(solution(dirs))