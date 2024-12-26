from math import sqrt

def solution(N, F, S, B, T, P, Q, W, O):
    answer = getResult(N, F, S, B, T, P, Q)
    return answer

def isPermutation(F):
    temp = sorted(F)

    for i in range(0, len(temp)):
        if temp[i] != i+1:
            return 0

    return 1

def getResult(N, F, S, B, T, P, Q):

    # 이전, 현재 위치 구하기
    before = getWhere(N, F, B)
    now = getWhere(N, S, B)

    d = getDirection(before, now)

    # 최종 p, q 구하기
    p = 60*abs(before - now)*P
    q = T * Q

    divisors = getDivisors(q)

    # p, q 가 서로소인 조건 채우기
    p, q = doDivisor(divisors, p, q)
    
    return d * (p/q)

def getWhere(N, F, B):
    result = -1

    for i in range(0, N-len(B)+1):
        temp = F[i:i+len(B)]

        cnt = 0
        for j in range(0, len(B)):
            if temp[j] != B[j]:
                break
            cnt += 1
        
        if cnt == 8:
            result = i+1
            break
    
    return result
    
def getDivisors(q):
    result = [1, q]

    for i in range(2, int(sqrt(q)+1)):
        if q%i == 0:
            result.append(i)
            result.append(q//i)
    
    return sorted(result)

def getDirection(before, now):
    # d 파악
    d = 0
    if before - now > 0:
        d = 1
    elif before - now < 0:
        d = -1

    return d

def doDivisor(divisors, p, q):
    for i in range(len(divisors)-1, -1, -1):
        if p%divisors[i] == 0:
            p = p//divisors[i]
            q = q//divisors[i]
            break

    return p, q