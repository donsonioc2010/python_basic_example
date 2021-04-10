# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))

full_name = "Kim, JongWon"
print(full_name.split(", "))

name_list = full_name.split(", ")
print(name_list[0])
print(name_list[1])

#white space 를 기준으로 split을 원하면 매개변수를 안주면 가능함
print("           \n\n    2 \t   \n 5 7 11 \n\n".split())

#split을 이용해 리스트를 만든 경우 해당 리스트는 모두 문자열이다.


print("1일: 3000".strip().split(": "))
