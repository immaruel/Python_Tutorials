'''
이미지 포맷 일괄 변경 프로그램 만들기
'''

from PIL import Image
import os
import argparse

#1. 파일 목록 가져오는 함수 생성(재귀 함수 이용)
def search_dir(dirname):
    result_file_list = []

    filenames = os.listdir(dirname) # 파일목록을 구해와서 리스트 형태로 담기
    for filename in filenames:
        full_path = os.path.join(dirname, filename) # 전체 경로 설정

        if os.path.isdir(full_path):
            if filenames != "convert":
                result_file_list.extend(search_dir(full_path))
        else:
            result_file_list.append(full_path)
    return result_file_list
file_list = search_dir("c:\\images")
#print(file_list)

# 2. 변경될 이미지가 새로운 폴더에 새롭게 생성되게 하기
new_format = ".png"

# 2-1. 파일경로 재정의
for file in file_list:
    new_folder = os.path.split(file)[0] + "\\convert"
    #print(new_folder)

    # 2-2 새롭게 만들어진 폴더에 새로운 파일 추가
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    src_filename = os.path.splitext(file)[0] # . 앞까지 추출
    new_file = new_folder + "\\" + src_filename.split("\\")[-1] + new_format
    print(new_file)

    # 2-3. 원본 폴더 내 확장자가 이미지 파일이 아닌 경우를 제와하고 새 폴더로 해당 파일 복사
    try:
        img = Image.open(file)
        img.verify() # verify함수는 이미지 유효성 검사
        img.close() # 세트르 붙여 닫아주자
        img = Image.open(file)
        img.save(new_file)
    except:
        pass