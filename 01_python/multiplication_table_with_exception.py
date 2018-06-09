# 과제 : 구구단을 2단에서 9단까지 제한
# 잘못된 값(에러) 입력한 경우 "2에서 9사이의 숫자 입력" 출력시키기
# 예외처리 및 재귀함수 활용

def dan_num():

    try:
        dan = int(input("구구단을 외우자. 2~9 사이의 숫자 입력: "))
        if dan > 1 and dan < 10:
            for num in range(10):
                print("{} * {} = {}".format(dan, num, dan * num))
        else:
            print("2단 ~ 9단 사이에서 선택해주세요")
            dan_num()
    except ValueError:
        print("숫자를 입력해주세요~~")
        dan_num()

dan_num()
