''' 
이미지 포맷 및 사이즈 일괄 변경 프로그램 만들기(두가지 기능 : 1.사이즈조정 2.확장자 변경)
'''
from PIL import Image
import os

class MyImage:
    def __init__(self, **kwargs): # 키워드형 인자 받기
        self.folder = kwargs.get("folder", None) #'folder'라는 키워드로 설정하고 'folder'로 키워드가 오지 않으면 디폴트를 None으로 설정한것 적용
        self.resize = kwargs.get("resize", False) # 'resize'를 할지 말지를 변수로 설정

        self.r_width = kwargs.get("r_width", 500) # 기본값 500으로 설정
        self.r_height = kwargs.get("r_height", 500) # 기본값 500으로 설정

        self.ext = kwargs.get("ext",None) # 변경될 확장자 설정
    
        self.newfolder = "__convert__" # 'convert'라는 폴더에 저장
        self.path_separator = "\\" # window에서 사용

        def is_valid_image(self, filename):
            try:
                img = Image.open(filename)
                img.verify()
                img.close()
                return True
            except:
                return False

    def search_dir(self, dirname): # class안의 함수이게에 self 넣기
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
    
    def change_format(self, img, filename, ext):
        new_folder = os.path.split(filename)[0] + self.path_separator + self.newfolder
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        
        src_filename = os.path.splitext(filename)[0]
        new_filename = new_folder + self.path_separator + src_filename.split(self.path_separator)[-1] + ext
        img.save(new_filename)
    
    def resize_image(self, filename):
        img = Image.open(filename)
        width, height = img.size
        if width < height: # 세로이미지일 경우
            aspect = height / self.r_height # 조정 사이즈 비율
            new_width = int(width / aspect)
            new_height = self.r_height
        else:
            aspect = width / self.r_width
            new_width = self.r_width
            new_height = int(height / aspect)

        
        new_size = (new_width, new_height) # 튜플형태
        return img.resize(new_size)

    # class동작함수 만들기
    def start(self):
        cnt_resize = 0
        cnt_format = 0
        if self.ext is None and self.resize is False:
            return(cnt_resize, cnt_format)

        file_list = self.search_dir(self.folder)

        for file in file_list:
            if not self.is_valid_image(file):
                continue
            if self.resize:
                img = self.resize_image(file)
                cnt_resize += 1
            else:
                img = Image.open(file)
            
            if self.ext is None:
                ext = str(file.split(self.path_separator)[-1].split(".")[-1]) # 확장자만 담음
    
            else:
                ext = self.ext
                cnt_format += 1
            
            if ext[0] != ".":
                ext = "." + ext
            self.change_format(img,file,ext)
        return(cnt_resize, cnt_format)
