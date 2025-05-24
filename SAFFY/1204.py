T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = arr.count(0)
    result = 0

    for score in range(1, 101):

        temp = arr.count(score)

        if(temp > max_value):
            max_value = temp
            result = score
        elif(temp == max_value):
            if score > result:
                result = score

    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////
