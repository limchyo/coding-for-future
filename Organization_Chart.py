name = input("이름을 입력하세요. ")
age = input("나이를 입력하세요. ")
gender = input("성별을 입력하세요. ")

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = Person(name, age, gender)

class Colleague(Person):
    position = "대리"

colleague = Colleague(name, age, gender)
print(person.name,person.age,person.gender,colleague.position)


# (고급) 직급 입력 추가
position = input("직급을 입력하세요. ")
class Colleague(Person):
    def __init__(self, position):
        self.position = position

colleague = Colleague(position)
print(person.name,person.age,person.gender,colleague.position)
