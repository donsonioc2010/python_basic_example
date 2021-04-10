def square(num):
    print("함수시작")
    return num * num
    print("함수 끝")# Dead Code 쓰기 X

print(square(3))
print("Hello World")

#옵셔널 파라미터
#옵셔널 파라미터는 뒤에 다 몰려있어야함. 개수는 상관없슴
def myself(name, age, national = "한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(national))

myself("코드잇", 1, "미국")
print("======")
myself("코드잇",1)