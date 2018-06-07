import random

menu = input("한식, 중식, 일식 중 어떤 걸 드시겠습니까? ")

한식 = ['계절밥상', '자연별곡', '풀잎채']
중식 = ['홍콩반점', '공화춘', '딘타이펑']
일식 = ['요시노야', '야요이켄', '코코이치방야']

if menu == '한식':
    print(random.choice(한식))
elif menu == '중식':
    print(random.choice(중식))
elif menu == '일식':
    print(random.choice(일식))

if menu == '한식':
    result = random.choice(한식)
elif menu == '중식':
    result = random.choice(중식)
elif menu == '일식':
    result = random.choice(일식)

print(result)
