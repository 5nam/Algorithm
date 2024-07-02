money = int(input('금액을 입력하세요 : '))
count = 0

if money % 10 != 0:
    print('N 은 항상 10의 배수')
    exit

if money >= 500:
    count += money // 500
    money = money % 500
if money >= 100:
    count += money // 100
    money = money % 100
if money >= 50:
    count += money // 50
    money = money % 50
if money >= 10:
    count += money // 10
    money = money % 10

print(count)
