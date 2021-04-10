# 리스트 (list)

numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"] # list 의 value를 요소라고함

print(numbers)
print(names)

# 인덱싱(indexing) 리스트 안에있는 요소를 가져오는 것이라 함
# 파이썬에서 리스트 시작은 0 번 부터 인덱스 시작
print(names[0])

print(numbers[-1])
print(numbers[-2]) #-1 부터 가장끝으로

# index slicing
numbers[0:4] # 0~3번방
numbers[2:] # 2번방 이후 전부
numbers[:3] # 2번방 까지


new_list = numbers[:3] #2번방까지가 대입됨