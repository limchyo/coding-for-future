class School:
    def __init__(self, name, year, address):
        self.name = name + "고등학교"
        self.year = "설립연도는 " + year
        self.address = "학교 위치는 " + address

school1 = School("김해", "1970년", "김해시 삼정동")
school2 = School("가야", "1990년", "김해시 내동")
school3 = School("분성", "2000년", "김해시 삼계동")

print(school1.name,school1.year,school1.address)
print(school2.name,school2.year,school2.address)
print(school3.name,school3.year,school3.address)
