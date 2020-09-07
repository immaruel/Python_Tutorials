'''
이미지 포맷 일괄 변경 프로그램 만들기
'''

from PIL import Image
import os
import argparse

# 1. 파일 목록 가져오는 함수 생성(재귀함수 이용)
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
file_list =  search_dir("c:\\images")

p = argparse.ArgumentParser() # 객체생성
p.add_argument(".f",type=str)#변경할것
p.add_argument(".e",type=str)#변경될것
args = p.parse_args()

if args.f is None or args.e is None:
    print("사용법: python changer.py -f <대상폴더> e <변환될 확장자")
else:
    new_format =args.e
    if new_format[0] != ".":
        new_format = "." + new_format

    file_list = search_dir(args.f)
    # 2. 변경될 이미지가 새로운 폴더(convert)에 새롭게 생성하게 하기
    for file in file_list: 
        # 2-1. 기존 'images'폴더안에 새끼 폴더 추가하기 
        new_folder = os.path.split(file)[0] + "\\convert"
        print(new_folder)
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        src_filename = os.path.splitext(file)[0]
        new_file = new_folder + "\\" + src_filename.split("\\")[-1] + new_format
        #print(new_file)

        #2-2. 새끼 폴더에 확장자를 바꿔 저장하기
        try:
            img = Image.open(file)
            img.varify() # verify()->이미지 유효성을 판단하는 함수
            img.close()
            img = Image.open(file)
            img.save(new_file)
        except:
            pass