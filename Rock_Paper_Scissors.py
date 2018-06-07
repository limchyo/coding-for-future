import random

computer_score=0
user_score=0

Rock_paper_scissors = ['가위', '바위', '보']

user_choice = input("가위, 바위, 보 중 하나를 고르시오. ")

computer_choice = Rock_paper_scissors[random.randint(0,2)]

while True:
    user_score == 3 and computer_score == 3

if user_choice == computer_choice:
    print("비겼습니다.")


elif user_choice == "가위":

    if computer_choice == "바위":
        computer_score += 1
        print("졌습니다.")
    else:
        user_score += 1
        print("이겼습니다.")


elif user_choice == "바위":

    if computer_choice == "보":
        computer_score += 1
        print("졌습니다.")
    else:
        user_score += 1
        print("이겼습니다.")


elif user_choice == "보":

    if computer_choice == "가위":
        computer_score += 1
        print("졌습니다")
    else:
        user_score += 1
        print("이겼습니다")

if user_score == 3:
    print("게임에서 승리하셨습니다")
elif computer_score == 3:
    print("게임에서 패배하셨습니다")

    # if(user_score >= 3 or computer_score >= 3):
    #     break
