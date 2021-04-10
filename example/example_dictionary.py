# 사전 (Dictionary)
# Key - value pair (키 - 값 - 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary))  # <class 'dict'>

#value 를 가져오는 법 my_dictionary[key값]
print(my_dictionary[2])

# 데이터를 추가하는법
my_dictionary[9] = 81
print(my_dictionary[9])

#사전의 키는 정수형일 필요가 없슴

my_family = {
    '엄마':'홍길동',
    '아빠':'일지매',
    '아들':'눕쨩',
    '딸':'돼지'
}

#모든 value만 확인하는 법
print(my_family.values())
#value값이 있나 확인 true false로 받음
print('딸' in my_family.values())
print('돼지' in my_family.values())
print('딸' in my_family.keys())

print('values')
for value in my_family.values():
    print(value)

for value in my_family.keys():
    print(value)

for key, value in my_family.items():
    print(key, value)

