def solution(N, stages):
    answer = [0] * (N+1)
    fail_rate = []
    players = len(stages)
    
    
    for i in range(len(stages)):
        answer[stages[i] - 1] += 1
    
    front_player = 0
    for i in range(len(answer)-1):
        
        if answer[i] == 0:
            fail = 0
        else:
            fail = answer[i] / (players - front_player)
        
        fail_rate.append([i+1, fail])
        front_player += answer[i]
        
    result = list(zip(*sorted(fail_rate, key = lambda x:(-x[1], x[0]))))
    
    return result[0]

arr = [2,1,2,6,2,4,3,3]

print(solution(5, arr))