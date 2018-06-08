# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit +1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")

# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# Enter number: """
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# coffee = 10
# money = 300
# while money:
#      print("돈을 받았으니 커피를 줍니다.")
#      coffee = coffee -1
#      print("남은 커피의 양은 %d개입니다." % coffee)
#      if not coffee:
#          print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#          break

# coffee = 10
# pokari = 10
# water = 10
# while True:
#     money = int(input("돈을 먼저 투입해주십시오: "))
#     beverage = input("커피(300원), 포카리(500원), 생수(100원) 중 택하시오: ")
#     if beverage == "커피":
#         if money == 300:
#             print("커피를 줍니다.")
#         coffee = coffee -1
#         if money > 300:
#             print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         else:
#             print("돈을 다시 돌려줍니다.")
#             print("남은 커피의 양은 %d개 입니다." % coffee)
#         if not coffee:
#             print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#
#     if beverage == "포카리":
#         if money == 500:
#             print("포카리를 줍니다.")
#         pokari = pokari -1
#         if money > 500:
#             print("거스름돈 %d를 주고 포카리를 줍니다." % (money -500))
#         else:
#             print("돈을 다시 돌려줍니다.")
#             print("남은 포카리의 양은 %d개 입니다." % pokari)
#         if not pokari:
#             print("포카리가 다 떨어졌습니다. 판매를 중지 합니다.")
#
#     if beverage == "생수":
#         if money == 100:
#             print("생수를 줍니다.")
#         water = water -1
#         if money > 100:
#             print("거스름돈 %d를 주고 생수를 줍니다." % (money -100))
#         else:
#             print("돈을 다시 돌려줍니다.")
#             print("남은 생수의 양은 %d개 입니다." % water)
#         if not water:
#             print("생수가 다 떨어졌습니다. 판매를 중지 합니다.")
#             break

# a = 0
# while a < 10:
#      a = a+1
#      if a % 2 == 1: continue
#      print(a)

# result = 0
# num = 1
# while num <= 100:
#     result += num # 전체 합을 구해주는 수식
#     num += 1 # 숫자를 하나씩 올려줌
# print(result)

# result = 0
# num = 1
# while num < 1000:
#     if num % 3 == 0: # 3의 배수 조건 만들기
#         result += num # 3의 배수 전체합
#     num += 1
# print(result)

# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# result = 0 # 전체합을 구하기 위한 발판
# while A: # for와 다르게 in 사용이 안됨
#     num = A.pop() # 리스트에서 순서대로 하나씩 뽑기 pop()
#     if num >= 50: # 50이상의 숫자를 변수로 지정
#         result += num # 위의 변수를 순차적으로 덧셈
# print(result) #전체합 출력

# a = 0
# while a < 5:
#     a += 1
#     print("*" * a)

# a = 0
# while True:
#     a += 1
#     if a > 5: break
#     print("*" * a)

# star = 7
# a = 0
# while True:
#     star -= 1
#     a += 0
#     if star = 1 and a = 6: break
#     print()

# star = 7  # 별의 갯수
# space = 0  # 공백의 갯수
# while star > 0:
#     print(' ' * space + '*' * star)  # 공백 + 별 출력
#     star -= 2  # 별의 갯수는 2씩 감소
#     space += 1 # 공백의 갯수는 1씩 증가

# for zero in range(5):
#     for one in range(5 - zero):
#         print("1", end ="")
#     print()

# for x in range(5):
#     for y in range(4-x):
#         print("0", end = "")
#
#     for z in range(x+1):
#         print("1", end = "")
#
#     print()

# for x in range(5):
#     for y in range(x):
#         print("0", end = "")
#
#     for z in range(5-x):
#         print("1", end = "")
#
#     print()

# for x in range(2):
#     print((2-x) * '0' + (x*2 + 1) * '1' + (2-x) * '0')
# for x in range(2, -1, -1): # 숫자 2부터 0까지 역순으로 -1씩 감소.
#     print((2-x) * '0' + (x*2 + 1) * '1' + (2-x) * '0')

# userInput = int(input("Please input side length of diamond: "))
# if userInput > 0:        # Prevents the computation of negative numbers
#     for i in range(userInput):
#         for s in range (userInput - i) :    # s is equivalent to to spaces
#             print(" ", end="")
#         for j in range((i * 2) - 1):
#             print("*", end="")
#         print()
#     for i in range(userInput, 0, -1):
#         for s in range (userInput - i) :
#             print(" ", end="")
#         for j in range((i * 2) - 1):
#             print("*", end="")
#         print()
