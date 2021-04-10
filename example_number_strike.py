import random

# 코드를 작성하세요.
answer = random.randint(1,20)

life = 5
count = 0
print(answer)
while True:
    if life == 0:
        print("아쉽습니다. 정답은 {}였습니다.".format(answer))
        break


    user_answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요:".format(life)))
    count += 1
    if answer == user_answer:
        print("축하합니다 {}번 만에 숫자를 맞혔습니다".format(answer))
        break
    elif user_answer > answer :
        print("Down")
    elif user_answer < answer :
        print("Up")

    life -= 1