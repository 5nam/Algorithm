def solution(prices):
    num = len(prices)
    result = []
    for i in range(num):
        if i == num:
            result.append(0)
            return
        for j in range(i+1, num):
            if prices[i] > prices[j]:
                break

        result.append(j-i)
    
    return result

print(solution([1,2,3,2,3]))