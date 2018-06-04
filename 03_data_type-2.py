list_a = [1, 2, 3]
print(type(list_a))

print(list_a[0])
print(list_a[1])
print(list_a[2])

print(list_a[1:2])

list_a.append(0)
print(list_a)
list_a.insert(0, 0)
print(list_a)

list_a.remove(0)
print(list_a)
# list_a.remove(3, 0) insert처럼 사용불가
# print(list_a)
list_a.clear()
print(list_a)


tuple_a = (1, 2, 3, 4)
print(tuple_a)
print(type(tuple_a))

dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])

dict_a["pen"] = "something to write"
print(dict_a)

set_a = set([1, 2, 3]) # 변수 설정시 set([]) 형태로 만든다
set_b = set([2, 4, 6])
print(set_a)
print(set_b)
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
