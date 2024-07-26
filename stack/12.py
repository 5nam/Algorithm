def solution(prices):
    n = len(prices)
    result = [0] * n

    stack = [0]
    for i in range(1, n):
        # 스택이 비어있지 않고, 이전 가격이 현재 가격보다 클 경우 가격이 하락했다고 볼 수 있음
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)

    # 스택에 남아있는 가격들은 끝까지 가격 하락이 없는 경우임
    while stack:
        j = stack.pop()
        result[j] = n - 1 - j

    return result

print(solution([1,2,3,2,3]))