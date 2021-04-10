#import module.example_calculator as calc
from module.example_calculator import add,multiply
#파일에서 함수가져오기 위에두개 사용가능 아래의 방식은 안불러온것은 사용 불가 모든 함수 부르기는 *


#print(calc.add(2, 5))
#print(calc.multiply(2, 4))

print(add(2, 5))
print(multiply(2, 4))

#standard module(이미 만들어진 기본 모듈)
import math

print(math.log10(100))
print(math.cos(0))
print(math.pi)

import random

print(random.random())

#randint는 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수입니다.
#randint(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴하는 것이죠.
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))

#uniform 은 소수를 리턴  randint와 다른 것은 리턴하는 값이 정수가 아니라 소수
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))


import os
#운영체제 관련
print(os.getlogin()) #현재 어떤계정으로 로그인되어있는지
print(os.getcwd())  #현재 파일의 위치