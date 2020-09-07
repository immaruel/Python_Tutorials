'''
썸네일에 여러가지 캡처이미지 몰아서 넣어주는 프로그램
'''

import cv2
import numpy as np # numpy의 별칭을 np 로 대신
import os
import mimetypes # 확장자 확인 라이브러리

# 0. 전체 컷 분리 함수
def get_video(filepath, capture_count=1):
    images = []

    # 1. 기본 동영상 정보
    cap = cv2.VideoCapture(filepath) # videoCapture라는 라이브러리 사용
    v_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 총 프레임수
    v_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 가로 해상도
    v_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 세로 해상도
    v_fps = cap.get(cv2.CAP_PROP_FPS) # 재생속도
    v_duration = v_frames / v_fps

    #3. 동영상 길이 n부분에 해당하는 컷 가져오기
    jump_frame = int(v_frames / capture_count) # 몇 부분씩 나눌지 설정

    for i in range(capture_count):
        pos = 1 + (jump_frame * i)
        cap.set(cv2.CAP_PROP_POS_FRAMS, pos) #캡처할 위치로 이동
        #2. 이미지 가져오기
        ret, frame = cap.read() # ret는 cap.read()함수 성공여부, frame:실제이미지
        if ret: # ret이 True면
            images.append(frame)
        cap.release() # 위에서 사용한 함수 release로 닫아주기
        return images

#4. n번만큼 분리된 컷을 한장으로 합쳐주는 함수
def create_collage(image_list, thumb_size=(210,137), rowcols=(5,5)):
    canvas_width = thumb_size[0] * rowcols[0] # 전체 가로길이
    canvas_height = thumb_size[1] * rowcols[1] # 전체 세로길이
    canvas = np.zeros(shape=(canvas_height, canvas_width, 3), dtype=np.uint8) # zeors:초기화, 3:컬러이미지이므로 3채널, 자료type은 부호없는 정수형(uint)

    cursor = [0,0] # 초기 커서위치
    for img in image_list:
        img = cv2.resize(img, thumb_size) # 컷 분리된 사진 사이즈만큼 리사아즈

        canvas[cursor[1]:cursor[1] + thumb_size[1], cursor[0]:cursor[0] + thumb_size[0]] = img # cursor[1] 세로로 이동, cursor[0] 가로로 이동
        cursor[0] += thumb_size[0]

        if cursor[0] >= rowcols[0] * thumb_size[0]:
            cursor[1] += thumb_size[1]
            cursor[0] = 0
    return canvas


#5. 사용자가 원하는 폴더에 있는 파일 가져오기 함수
def search_dir(dirname):
    result_file_lists = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filepath = os.path.join(dirname, filename)
        if os.path.isdir(full_filepath):
            result_file_lists.extend(search_dir(full_filepath))
        else:
            mimetypes = "" if mimetypes.guess_type(full_filepath)[0] is None else mimetypes.guess_type(full_filepath)[0]
            if mimetype.find("video") >= 0:
                result_file_lists.append(full_filepath)
    return result_file_lists

#6. 쓰기 함수 만들기
def my_imwrite(filename, img):
    try:
        ext = os.path.splitext(filename)[-1] # 확장자만 분리
        result, buffer = cv2.imencode(ext, img)
        if result:
            with open(filename, mode="wb" ) as f:
                buffer.tofile(f)
                return Tru
        else:
            return True
    except Exception as e:
        print(e)
        return False

target = "c:\\test"
filelist = search_dir(target)
for file in filelist:
    new_filename = os.path.splitext[0] + ".jpg"
    images = get_video(filepath, 9)
    canvas = create_collage(images, rowcols=(3,3))
    my_imwrite(new_filename,canvas)