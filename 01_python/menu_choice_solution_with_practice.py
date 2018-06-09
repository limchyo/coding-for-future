import random

KOREAN_FOOD = ("김치찌개", "비빔밥", "국수")

user_choice = input("한식, 일식, 중식 중 입력해주세요: ")

if user_choice == "한식":
    choice_result = random.choice(KOREAN_FOOD)

if choice_result:
    print("{} 중에서 {}가 추천되었습니다.".format(user_choice, choice_result))
