for j in range(2):
    for i in range(2):
        print('i:{}, j:{}'.format(i,j))

dan = int(input("몇 단을 출력하시겠습니까? "))
for num in range(10):
    # print(dan * num)
    print("{} * {} = {}".format(dan, num, dan * num))

# 과제 : 구구단을 2단에서 9단까지 제한

dan = int(input("몇 단을 출력하시겠습니까? "))
if dan > 1 and dan < 10:
    for num in range(10):
        print("{} * {} = {}".format(dan, num, dan * num))
else:
    print("2단 ~ 9단 사이에서 선택해주세요")
