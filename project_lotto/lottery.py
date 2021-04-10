from random import randint


def generate_numbers(n):
    # 코드를 작성하세요.
    number_list = []

    while len(number_list) < n:
        num = randint(1, 45)
        if num not in number_list:
            number_list.append(num)

    return number_list


def draw_winning_numbers():
    # 코드를 작성하세요.
    numbers = generate_numbers(7)
    return sorted(numbers[:6]) + numbers[6:]

def count_matching_numbers(list_1, list_2):
    #집합교집합 https://wikidocs.net/1015
    return len(set(list_1).intersection(list_2))


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    answer_val = count_matching_numbers(numbers, winning_numbers[:6])
    if answer_val == 6:
        return 1000000000
    elif count_matching_numbers(numbers, winning_numbers) == 6:
        return 50000000
    elif count_matching_numbers(numbers, winning_numbers[:6]) == 5:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers[:6]) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers[:6]) == 3:
        return 5000
    else :
        return 0

