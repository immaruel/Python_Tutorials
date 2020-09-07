# 파이썬에서 파일을 읽고 쓰기

file = open("sample3.txt", mode="w", encoding="utf-8")
file.write("안녕 파이썬")
file.close()

with open("sample3.txt", mode="r", encoding="utf-8")as s, open("sample4.txt",mode="w", encoding="utf=-8")as t:
    t.write(s.read().replace("파이썬","가즈아~"))