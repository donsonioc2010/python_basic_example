#이번에는 random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램을 바꿔 보세요.
word_list = []
with open("vocabulary.txt", "r", encoding="UTF-8") as f:
    for line in f:
        word_list.append(line.strip().split(": "))

import random

while True:
    quest_num = random.randint(0, len(word_list) - 1)
    answer = input("{}: ".format(word_list[quest_num][1]))

    if answer == 'q':
        break
    elif answer == word_list[quest_num][0]:
        print("맞았습니다!\n")
    else:
        print("틀렸습니다!\n")