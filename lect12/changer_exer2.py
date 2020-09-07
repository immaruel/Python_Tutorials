'''
해당 이미지 포맷 일괄 변경 프로그램 만들기
'''

from PIL import Image # pillow 라이브러리 사용
import os
import argparse # 실행시 인자값을 받아 실행할수 있도록 해당 라이브러리 사용

# 1. 해당 폴더 안에 있는 파일 모두 리스트 형태로 정리
def search_dir(dirname):
    result_file_list = []

    filenames = os.listdir(dirname) # 폴더와 파일 이름대로 정리해서 리스트 형태로 정리
    for filename in filenames:
        full_path = os.path.join(dirname, filename) # 전체 경로 설정

        if os.path.isdir(full_path):
            if filename != "convert":
                result_file_list.extend(search_dir(full_path)) # 재귀함수 사용
            else:
                result_file_list.append(full_path)
        return result_file_list
file_list = search_dir("c:\\images")
#print(search_dir("c:\\images"))

#2. 새롭게 만들어진 폴더(convert)에 복사된 파일 추가
new_format = ".png" 
#2-1 파일 경로 재정의
for file in file_list:
    new_folder = os.path.split(file)[0] + "\\convert"
    #print(new_folder)
    # 2-2 새롭게 만들어진 폴더에 새로운 파일 추가
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    src_filename = os.path.splitext(file)[0]
    new_file = new_folder +  "\\" + src_filename.split("\\")[-1] + new_format
    print(new_file)

    # 2-3 원본 폴더 내 확장가 이미지가 아닌 것은 제외시키기
    try:
        img = Image.open(file)
        img.verify()
        img.close()
        img = Image.open(file)
        img.save(new_file)
    except:
        pass