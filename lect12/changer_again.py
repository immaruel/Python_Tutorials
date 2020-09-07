'''
해당 이미지 포맷 일괄 변경 프로그램 만들기
'''
from PIL import Image
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

#print(search_dir("c:\\images"))

#3. 실행시 인자값을 받아 실행할수 있도록 코딩
p = argparse.ArgumentParser() # 객체 생성
p.add_argument("-f",type=str) # 변경할 형태 : str
p.add_argument("-e",type=str) # 변경될 형태 : str
args = p.parse_args()

if args.f is None or args.e is None:
    print("사용법: python changer.py -f <대상폴더> e <변환될 확장자")
else:
   new_format =args.e
   if new_format[0] != ".":
       new_format = "." + new_format
    file_list = search_dir(args.f)
    # 2. 원본 폴더내 원본 파일을 변경후 다른 확장자로 새로운 폴더 안에 정리
    #file_list = search_dir("c:\\images")
    # 2-1. 원본 폴더 내 새로운 폴더 생성
    for file in file_list:
        new_folder = os.path.split(file)[0] + "\\convert"
        #print(new_folder)
        
        #2-2. 새롭게 만들어진 폴더에 새로운 파일 추가
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        src_filename= os.path.splitext(file)[0]
        new_file = new_folder + "\\" + src_filename.split("\\")[-1] + new_format
        #print(new_file)

        #2-3. 원본 폴더 내 확장자가 이미지 파일이 아닌 경우는 제외하고 새 폴더로 해당 파일을 복사
        try:
            img = Image.open(file)
            img.verify() # verify:이미지 유효성 확인 함수 
            img.close() # 항상 세트로 선언해주어야함
            img = Image.open(file)
            img.save(new_file)
        except:
            pass
