# 파이썬에서 파일을 읽고 쓰기

file = open("sample.txt", mode="w", encoding="utf-8")
file.write("안녕 파이썬 ")
file.close()

with open("sample.txt", mode="r", encoding="utf-8") as s, open("sample2.txt",mode="w", encoding="utf-8") as t:
    t.write(s.read().replace("파이썬","python~"))
 
file = open("sample5.txt", mode="w", encoding="utf-8")
file.write("드래곤본")
file.close()

with open("sample5.txt", mode="r", encoding="utf-8") as a, open("sample6.txt",mode="w", encoding="utf-8") as b:
    b.write(a.read().replace("드래곤볼","베지터"))

