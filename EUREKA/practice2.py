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
    
    gcd = getGCD(p, q)
    if(gcd != 1):
        p = p//gcd
        q = q//gcd
    
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

def getGCD(p, q):
    if q == 0:
        return p
    
    return getGCD(q, p%q)

def getDirection(before, now):
    # d 파악
    d = 0
    if before - now > 0:
        d = 1
    elif before - now < 0:
        d = -1

    return d

N = 10
F = [1,2,3,4,5,6,7,8,0,0]
S = [0,0,1,2,3,4,5,6,7,8]
B = [1,2,3,4,5,6,7,8]
T = 60
P = 13
Q = 11

getResult(N, F, S, B, T, P, Q)