# 랜덤 뽑기
import random
random_list = [1,2,3,4,5]

print(random.choice(random_list))
print(random.randint(1,6))

# 인자 길이 줄여서 출력하기
lotto = random.choice(random_list)
print(lotto)

# 여러 개 동시에 뽑기
print(random.sample(random_list,3))
