#string format

#day
year = 2021
month = 4
day = 29

print(" 오늘은 "+str(year)+"년 "+str(month)+"월 "+str(day)+"일 ")
print(" 오늘은 {}년 {}월 {}일".format(year, month, day))

date_string = " 오늘은 {}년 {}월 {}일"
print(date_string.format(year, month, day))

mr_yu = "유재석"
mr_park = "박지성"
mr_bill = "빌게이츠"
print("저는 {2}, {0}, {1}를 좋아합니다".format(mr_yu, mr_park, mr_bill))

num1 = 1
num2 = 3
print("{0} 나누기 {1} 은 {2}입니다".format(num1, num2, num1/num2))
print("{0} 나누기 {1} 은 {2:.2f}입니다".format(num1, num2, num1/num2))