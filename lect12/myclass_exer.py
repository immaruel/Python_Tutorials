'''
이미지 파일 의 확장자 or 사이즈 변경 프로그램 만들기
'''
from PIL import Image
import os

class MyImage:
    def __init__(self, **kwargs): # 키워드형 인자 받기
        self.folder = kwargs.get("folder",None) # 'folder'라는 키워드가 오면 사용하지만 초기값은 None으로 두기
        self.resize = kwargs.get("resize",False) # resize 할지 말지 결정
        
        self.r_width = kwargs.get("r_width",500) # 임의로 가로값을 500으로 두기
        self.r_height = kwargs.get("r_height",500) # 임의로 세로값을 500으로 두기

        self.ext = kwargs.get("ext",None) # 변경될 확장자 키워드를 ext로 받고 초기값은 None으로 두자

        self.newfolder = "__convert__" # 새롭게 만들 폴더명은 'convert'로 명명
        self.path_separator = "\\" # window는 파일경로를 '\\'로 한다
    
    # 0. 각각의 기능을 수행할 함수 만들기

    # 1. 파일 열때 유효성 검사 함수
    def is_valid_image(self, filename):
        try:
            img = Image.open(filename) # 이미지파일 열기
            img.vertify() # 파일 유효성 검사
            img.close() # 파일 닫기
            return True
        except:
            return False

    # 2. 파일 목록 가져오는 함수 (재귀함수 사용)
    def search_dir(self, dirname): # class안의 함수이기에 self 넣자
        result_file_list = [] # 리스트 한개 선언

        filenames - os.listdidr(dirname) # 파일목록을 가져와 리스트 형태로 담기
        for filename in filenames:
            full_path = os.path.join(dirname, filename) # 전체 경로 
            
            if os.path.isdir(full_path):
                if filenames != self.newfolder:
                    continue
                result_file_list.extend(self.search_dir(full_path))
            else:
                result_file_list.append(full_path)
        return result_file_list
    
    # 3. 확장자 바꾸기 함수
    def change_format(self, img, filename, ext): # 사용자로 부터 해당이미지, 파일명, 바꿔줄 확장자 입력받기
        new_folder = os.path.split(filename)[0] + self.path_separator + self.newfolder # 파일명 정의
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        src_filename = os.path.splitext(filename)[0]
        new_filename = new_folder + path_separator + src_filename.split(self.path_separator)[-1] + ext
        img.save(new_filename) # 새로운 확장자 이미지 파일 저장

    # 4. 리사이즈 기능추가 함수
    def resize_image(self, filename): # 사용자로부터 이미지파일명 입력받기
        img = Image.open(filename) # 파일열기
        width, height = img.size # 원본 이미지 파일 사이즈 저장
        if width < height: # '세로 > 가로'인 이미지 파일일 경우
            aspect = height / self.r_width # 변경할 이미지 사이즈 비율 
            new_width = int(width / aspect)  # hegiht에서 변경된 사이즈 만큼 width 에서 비율 적용해서 변경하기
            new_height = self.r_height
        else: # '세로 < 가로'인 이미지 파일일 경우
            aspect - width / self.r_width
            new_width = self.r_width
            new_height = int(height / aspect)
        
        new_size = (new_height, new_width) # 변경된 이미지 파이은 튜플 형태로 저장
        return img.resize(new_size)

    # 5. 위에서 만든 class를 동작시키는 함수
    def start(self):
        cnt_resize = 0 # 리사이즈 한 횟수
        cnt_format = 0 # 확장자 변경한 횟수
        
        if self.ext is None and self.resize is False: # 확장자,리사이징 둘다 안할 경우
            return (cnt_format, cnt_resize)
        
        file_list = self.search_dir(self.folder) # 2번함수 : 파일 목록 가져오기
        for file in file_list:
            if not self.is_valid_image(file): # 1번함수 : 파일 유효성 체크 함수
                continue

            if self.resize: # 리사이즈 할 경우
                img = self.resize_image(file) # 4번함수 : 리사이즈 변경 함수
                cnt_resize += 1 # 리사이징 후 횟수 +1 해주기
            else: # 리사이즈 안할 경우
                img = Image.open(file) # 리사이즈 안하더라도 4번함수에 의해 이미지 파일이 열리므로 일단 선언!
            
            if self.ext is None: #확장자 변경 안할 경우
                ext = str(file.split(self.path_separator)[-1]).split(".")[-1] # 확장자 변경 안하므로 원래 확장자 구하기
            else:
                ext = self.ext

            if ext[0] != ".":
                ext = "." + ext
            self.change_format(img, file, ext)
        return (cnt_resize, cnt_format)