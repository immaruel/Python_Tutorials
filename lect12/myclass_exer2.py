''''
이미지 포맷 및 사이즈 일괄 변경 프로그램 만들기 (두가지 기능 : 1.사이즈조정, 2.확장자변경)
''''
from PIL import Image
import os

class MyImage:
    def __init__(self, **kwargs): # 키워드형 인자 받기
        self.folder = kwargs.get("folder", None) # 'folder'라는 키워드가 오면 쓰지만 전까지 None
        self.resize = kwargs.get("resize", False) # resize하지말지 결정

        self.r_width = kwargs.get("r_width", 500) # 임의의 기본값 500으로 설정
        self.r_height = kwargs.get("r_height", 500) # 임의의 기본값 500으로 설정

        self.ext = kwargs.get("ext",None) # 변경된 확장자 키워드 받기

        self.newfolder = "__convert__" # 새롭게 만들어질 폴더명을 convert라 명명
        self.path_separator = "\\" # window에선 리눅스와 다르게 사용

        #0. 각 기능을 수행할 함수를 각 각 만들기

        #1. 파일 열때 유효성 검사 수행 함수
        def is_valid_image(self, filename):
            try:
                img = Image.open(filename)
                img = verify()
                img.close()
                return True
            except:
                return False
        
        #2. 파일 목록 가져오는 함수(재귀함수 사용)
        def search_dir(self, dirname): # class안의 함수이게 self 붙여주자
        result_file_list = []

        filenames = os.listdir(dirname) # 파일 목록을 구해와서 리스트 형태로 담기
        for filename in filenames:
            full_path = os.path.join(dirname, filename) # 전체 경로 설정

            if os.path.isdir(full_path):
                if filenames != self.newfolder:
                    continue
                result_file_list.extend(self.search_dir(full_path))
                else:
                    result_file_list.append(full_path)
            return result_file_list

        #3. 확장자를 바꿔주는 함수
        def change_format(self, img,filename,ext):
            new_folder =os.path.split(filename)[0] + self.path_separator + self.newfolder
            if not os.path.exists(new_folder):
                os.mkdir(new_folder)
            src_filename = os.path.splitext(filename)[0] # . 앞까지 짜르기
            new_filename = new_folder + path_separator + src_filename.split(self.path_separator)[-1] + ext 
            img.save(new_filename)

        #4. 리사이즈 기능 추가 함수
        def resize_image(self, filename):
            img = Image.open(filename)
            width, height = img.size # 원본 이미지 파일 사이즈 저장
            if width < height: # '세로 > 가로'인 이미지 파일일 경우
                aspect = height / self.r_width # 변경할 이미지 사이즈 비율 
                new_width = int(width / aspect)  # hegiht에서 변경된 사이즈 만큼 width 에서 비율 적용해서 변경하기
                new_height = self.r_height
            else: # '세로 < 가로'인 이미지 파일일 경우
                aspect - width / self.r_width
                new_width = self.r_width
                new_height = int(height / aspect)
            new_size = (new_height, new_width)
            
            return img.resize(new_size)

        #5. 위에서 만든 class를 동작시키는 함수
        def start(self):
            cnt_reszie =0 
            cnt_format =0

            if self.ext is None and self.resize is False:
                return (cnt_format, cnt_reszie)
            
            file_list = self.search_dir(self.folder) # 2번함수 :파일목록 가져오기
            for file in file_list:
                if not self.is_valid_image: # 1번함수 : 파일 유효성 체크 함수
                    continue

                if self.resize: # 리사이즈 할 경우
                    img = self.resize_image(file)
                    cnt_resize += 1
                else:
                    img = Image.open(file)
                
                if self.ext is None:
                    ext = str(file.split(self.path_separator)[-1]).split(".")[-1] # 확장자 변경 안하므로 원래 확장자 구하기
                else:
                    ext = self.ext
                
                if ext[0] != ".":
                ext = "." + ext
            self.change_format(img, file, ext)
        return (cnt_resize, cnt_format)