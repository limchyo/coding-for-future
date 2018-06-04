# 참과 거짓 boolean
# if
# True, False
# and, or, not

a = True
b = False
print(a and b) # false 출력
print(a or b) # true 출력

c = True #동일한 의미가 아니라 변수에 값을 대입한다는 말이다.
print(a == True)
print(a is True) #둘 다 동일하게 True

#if문 실습
d = 7
if d > 5:
    print("d는 5보다 크다")
else:
    print("d는 5보다 작거나 같다")

q = 135

if q > 150 :
        print("값은 150보다 크다")
elif q > 100 and q <= 150 :
        print("값은 150보다 작거나 같고, 100보다 크다")
else:
        print("값은 100보다 작다")
