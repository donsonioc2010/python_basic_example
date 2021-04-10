from random import randint

#랜덤숫자 3개 생성
def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        random_num = randint(0, 9)
        if random_num not in  numbers:
            numbers.append(random_num)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    new_guess = []

    count = 1
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    while len(new_guess) < 3:
        user_number = int(input("{}번째 숫자를 입력하세요:".format(count)))

        if user_number < 0 or user_number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")
        elif user_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요")
        else:
            new_guess.append(user_number)
            count += 1

    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    for i in range(0, len(solution), 1) :
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    # ball_count = len(set(guess).intersection(solution)) # ball 갯수
    # ball_count = ball_count - strike_count


    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

print(ANSWER)
while True:
    guess_list = take_guess()
    strike,ball = get_score(guess_list, ANSWER)
    tries += 1
    if strike == 3:
        break
    else:
        print("{}S {}B\n".format(strike, ball))


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
