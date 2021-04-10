def hello(name): #Function의 헤더역할 (시작)
    print("Hello!")
    print(name)
    print("Welcome To Codeit")


hello("Noob")
#Tab을 해서 들여쓰게되면 hello Function으로 인식함으로 들여쓰면 안됨!


#여러개의 파라미터를 받아야 하는 경우
def print_sum(a, b, c, d):
    print(a+b+c*d)

print_sum(3,6,7,9)