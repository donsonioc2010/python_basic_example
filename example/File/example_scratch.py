# strip 앞뒤로 있는 화이트 스페이스 (" ", "\t", "\n")를 제거해주는 역할

print("          abc            def            ".strip())

with open('chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())

