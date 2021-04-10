# r = read, w = write 파일위치 틀리면 경로 적어줘야함 data/chicken.txt같이
with open('chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line)