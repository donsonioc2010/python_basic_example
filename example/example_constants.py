#상수

# 파이
PI = 3.14
#상수는 대문자로만 작성함. 구분을 하기 위함임

# 반지름을 받아서 원넓이
def calculate_area(r):
    return PI * r * r


radius = 4#반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))