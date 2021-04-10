#datetime에 대한 라이브러리
import datetime

#datetime 값 생성
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

#오늘날짜 받는법
today = datetime.datetime.now()
print(today)
print(type(today))

#datetime값 사이의 시간을 알고싶은 경우 (시간뺴는경우)
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))

#반대로 시간 더하는 경우
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)


#datetime 년도/월등 추출하는법
today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초


#datetime 포메팅
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))