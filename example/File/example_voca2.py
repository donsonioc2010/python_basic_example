with open("vocabulary.txt", "r", encoding="UTF-8") as f :
    for line in f:
        word_list = line.strip().split(": ")
        english_word = word_list[0]
        korean_word = word_list[1]

        answer = input("{}:".format(korean_word))
        if answer == english_word :
            print("맞았습니다!")
        else :
            print("아쉽습니다. 정답은 {}입니다.".format(english_word))