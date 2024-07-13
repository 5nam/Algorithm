def solution(N, stages):
    # 스테이지마다 몇 명이 있는지 세기
    players = len(stages)
    stage_count = [0] * (N+1)
    
    
    for index in range(players):
        stage_count[stages[index] -1] += 1
    
    # 실패율 구하기
    player_num = 0
    stage_fail = []
    
    for index in range(N):
        if stage_count[index] == 0:
            stage_fail.append([index+1, 0])
            continue
        
        fail_rate = stage_count[index] / (players - player_num)
        
        stage_fail.append([index+1, fail_rate])
        player_num += stage_count[index]
    
    # 1) 실패율 기준으로 2) 인덱스 기준으로 정렬
    
    sorted_array = sorted(stage_fail, key=lambda x: (-x[1], x[0]))
    
    answer = list(zip(*sorted_array))
        
    return answer[0]

print(solution(5, [2,1,2,6,2,4,3,3]))