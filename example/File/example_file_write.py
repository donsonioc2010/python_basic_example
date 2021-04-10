
# w = write, a = append a의 경우 파일이 없으면 파일을 만든후에 추가함, w는 덮어씀
with open('new_file.txt', 'w') as f :
    f.write("Hellol Wrold")
    f.write("My name is Jong1\n")