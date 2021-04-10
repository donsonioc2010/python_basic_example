# list의 함수들

numbers = []
print("입력전")
print(numbers)
print(len(numbers))


numbers.append(5)
numbers.append(8)
print("입력후")
print(numbers)
print(len(numbers))

number = [2, 3, 5, 7, 11, 13]

print(number[3])
del number[3]
print(number[3])
number.insert(4,37)
print(number)

#len = 해당 리스트 길이 파악
# append = 마지막에 추가
# insert(index, value) = index값에 value 추가