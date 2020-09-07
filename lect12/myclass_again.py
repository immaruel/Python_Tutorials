'''
이미지파일의 확장자 or 사이즈 변경 프로그램 만들기
'''

from PIL import Image
import os

class MyImage:
    def __init__(self, **kwargs): # 키워드형 인자 받기
        self.folder = kwargs.get("folder",None) # 'folder'라는 키워드 오면 쓸때지만 초기값은 None으로 설정
        self.resize = kwargs.get("resize",False) # resize를 할지 말지를 결정할 변수 설정
    
        self.r_width= kwargs.get("r_width", 500) # 임의로 기본값 500으로 설정
        self.r_height= kwargs.get("r_height", 500) # 임의로 기본값 500으로 설정

        self.ext = kwargs.get("ext",None) # 변경될 확장자 키워드를 ext로 받고 초기값은 None으로 설정

        self.newfolder = "__convert__" # 새롭게 만들 폴더를 convert로 명명
        self.path_separator = "\\" # window에서 쓸수 있는 것으로 변수 설정해주기 리눅스는 다르므로

    # 0. 각 기능을 할 함수들을 따로 따로 만들어 놓기

    # 1. 파일 열때 유효성 검사 함수 
    def is_valid_image(self, filename):
        try:
            img = Image.open(filename)
            img.verify()
            img.close()
            return True
        except:
            return False
    
    # 2. 파일 목록 가져오는 함수(재귀함수 이용)
    def search_dir(self, dirname): # class안의 함수이기에 self 넣기
        result_file_list = []
        
        filenames = os.listdir(dirname) # 파일목록을 구해와서 리스트 형태로 담기
        for filename in filenames:
            full_path = os.path.join(dirname, filename) # 전체 경로 설정
            
            if os.path.isdir(full_path):
                if filenames != self.newfolder:
                    continue
                result_file_list.extend(self.search_dir(full_path))
            else:
                result_file_list.append(full_path)
        return result_file_list
        
    # 3. 확장자 바꿔주는 함수
    def change_format(self, img, filename, ext): # 사용자로부터 해당이미지, 파일이름. 바꿔줄 확장자 입력 받기
        new_folder = os.path.split(filename)[0] + self.path_separator + self.newfolder
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        src_filename = os.path.splitext(filename)[0]
        new_filename = new_folder + path_separator + src_filename.split(self.path_separator)[-1] + ext
        img.save(new_filename)

    # 4. 리사아즈 기능 함수
    def resize_image(self, filename): # 사용자로부터 파일이름 입력 받기
        img = Image.open(filename)
        width, height = img.size # 원본 이미지 파일 사이즈 저장
        if width < height: # 세로 이미지일 경우
            aspect = height / self.r_width # 변경할 사이즈 비율
            new_width = int(width / aspect) # height에서 변경된 사이즈 만큼 width에서 비율 적용해서 변경하기
            new_height = self.r_height
        else: #가로 이미지일 경우
            aspect = width / self.r_width
            new_width = self.r_width
            new_height = int(height / aspect)
        
        new_size = (new_width, new_height) # 변경된 이미지파일은 튜플 형태로 저장
        return img.resize(new_size)
    
    # 5. 위에서 만든 class를 동작시키는 함수
    def start(self):
        cnt_resize = 0 # 리사이즈 한 횟수
        cnt_format = 0 # 확장자 변경한 횟수

        if self.ext is None and self.resize is False: # 확장자도 변경 안하고 사이즈 변경도 안할 경우
            retrun (cnt_format, cnt_format) # 할일 없이 리턴시킴

        file_list = self.search_dir(self.folder) # 2번 함수 : 파일 목록 리스트 가져오기
        for file in file_list:
            if not self.is_valid_image(file): # 1번 함수 : 파일 유효성 함수 
                continue
            
            if self.resize: # 리사이즈를 할경우
                img = self.resize_image(file) # 4번 함수 : 리사이즈 변경 함수+
                cnt_resize += 1
            else: # 리사이즈 안할경우
                img = Image.open(file) # 라사이즈를 안하더라도 4번함수에 의해 이미지 파일이 열리므로
            
            if self.ext is None: # 확장자 변경 안할 경우
                ext = str(file.split(self.path_separator)[-1]).split(".")[-1] # 확장자 변경 안하므로 원래 확장자 구하기
            else: # 확장자 변경할 경우
                ext = self.ext

            if ext[0] != ".":
                ext = "." + ext
            self.change_format(img, file, ext)
        return(cnt_resize, cnt_format)
