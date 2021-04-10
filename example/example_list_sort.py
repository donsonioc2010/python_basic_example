numbers = [19, 13, 2, 5, 3, 11, 7, 17]

print(numbers)
new_numbers = sorted(numbers) #작은수부터 , 파라미터 value를 건들지 않음
print(new_numbers)

new_numbers = sorted(numbers, reverse=True) #큰값부터
print(new_numbers)

print(numbers.sort()) #.sort 는 넘어온 파라미터 리스트를 소팅함 역순은 .sort(reverse=True) 를 사용하면 된다