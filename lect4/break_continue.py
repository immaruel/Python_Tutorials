# 반복문 while,for 

# num = 0
# while True:
#     print(num)
#     num += 1

#     if num == 10:
#         break

# num = 0 
# while num < 10:
#     num += 1
#     if num == 5:
#         continue
#     print(num)

point = [1,2,3,4,8]
for p in point:
    if p < 4:
        continue
    print("{}점입니다".format(p))