def solution(n, k, cmd):
    deleted = []

    up = [i - 1 for i in range(n+2)]
    down = [i + 1 for i in range(n+1)]

    # 현재 위치를 나타내는 인덱스
    k += 1

    # 주어진 명령어(cmd) 리스트를 하나씩 처리
    for value in cmd:
        # 현재 위치를 삭제하고 그 다음 위치로 이동
        if value.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]

            k = up[k] if n < down[k] else down[k] # n < down[k] 즉, 현재 위치의 아래가 n 보다 크면 현재 위치가 마지막 행인 것이므로 up[k] 로 k 를 갱신, 아니라면 down[k] 로 k 를 갱신
        
        # 가장 최근에 삭제된 행을 복원
        elif value.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore

        # U 또는 D 를 사용하여 현재 위치를 아래로 이동
        else:
            action, num = value.split(" ")

            if action == "U":
                for _  in range(int(num)):
                    k = up[k] # 상대적 위치로 해놓은 리스트를 통해 이동한 현재 위치 반영해주는 것(입력된 숫자만큼)
            elif action == "D":
                for _ in range(int(num)):
                    k = down[k] # 상대적 위치로 해놓은 리스트를 통해 이동한 현재 위치 반영해주는 것(입력되 숫자만큼)
    
    # 삭제된 행의 위치에 'X' 를, 그렇지 않은 행의 위치에 'O'를 포함하는 문자열 반환
    result = ["O"] * n

    for index in deleted:
        result[index - 1] = "X"
    
    return "".join(result)

cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(8,2,cmd))