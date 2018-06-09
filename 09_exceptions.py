# exceptions



# ZeroDivisionError

# 1 / 0

def divide_by(first, second):

    try: #함수 실행

        return first / second # 반환 값

    # except:

    except ZeroDivisionError: #예외처리할 에러

        return "0으로 나눌 수 없습니다."
#
#
#
# # 4 / 2 = 2
# #
print(divide_by(4, 2))

print(divide_by(4, 0)) # 분모가 0이므로 에러발생
                        # 에러 대신 반환 값 출력



# 예외 만들기

# Exception

class EvenNumberDevisionError(Exception): #상속

    pass # try와 return 생략



def divide_by_odd_number(first, second):

    if second % 2 == 0:

        raise EvenNumberDevisionError
            # 분모에 짝수를 넣으면 에러 발생
    else:

        return first / second



print(divide_by_odd_number(6, 3))
    # 분모가 홀수이므로 정상작동
print(divide_by_odd_number(6, 2))
    # 분모가 짝수이므로 에러발생
