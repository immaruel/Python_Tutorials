'''
내 컴퓨터의 동영상 썸네일 콜라주를 자동으로 만들어주는 프로그램
'''

import cv2 # opecCV 라이브러리
import os
import numpy as np # numpy라이브러리를 np로 별칭 사용
import mimetypes # 확장자 확인 라이브러리


#2. 비디오 가져오기 함수
def get_video(filepath, capture_count=1):
    images = []
    # 1. 동영상 정보 받아오기
    filepath = "c:\\test\\movie2.mp4"

    cap = cv2.VideoCapture(filepath) # VideoCapture 라이브러리 사용
    v_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 총 프레임수
    v_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 가로 해상도
    V_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 세로 해상도
    v_fps = cap.get(cv2.CAP_PROP_FPS) # 초당 프레임 시간
    v_duration = v_frames / v_fps
    #print(v_frames, v_width, V_height,v_fps, v_duration) # 832 852 480 23.999769232988143 34.667

    jump_frame = v_frames / capture_count # 총 동영상 길이당 나눌 캡처해서 나눌 프레임수 계산 설정

    for i in range(capture_count):
        pos = 1 + (jump_frame * i) # 다음 커서 위치 설정
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos) # 커서 설정
        ret, frame = cap.read()
        if ret: # ret이 True이면
            cv2.imshow("frame",frame)
            cv2.WaitKey(0)
            cv2.destroyAllWindows()
            images.append(frame)
    cap.release() # cap함수를 사용하였으면 release 붙여주기
    return images

#3. n 번 나뉜 캡처본을 합쳐주는 함수
def create_collage(image_list, thumb_size=(210,137), rowcols=(5,5)): # thumb_size(나눠 들어갈 캡처본 한장크기)
    canvas_width = thumb_size[0] * rowcols[0] # 전체 가로 길이
    canvas_height = thumb_size[1] * rowcols[1] # 전체 세로 길이
    canvas = np.zeros(shape=(canvas_height, canvas_width, 3), dtype=np.uint8) # zeors:초기화, 3:컬러이미지이므로 3채널, 자료type은 부호없는 정수형(uint)
    canvas.fill(320) # 나눠진 공란 채울 색 설정

    # 3-1 커서가 이동하면서 다음 캡처본으로 넘어갈수 있는 기능 추가
    cursor = [0,0]
    for img in image_list:
        img = cv2.resize(img, thumb_size) # thumb_size만큼 리사이즈
        canvas[cursor[1]:cursor[1] + thumb_size[1], cursor[0]:cursor[0] + thumb_size[0]] = img # cursor[1] 세로로 이동, cursor[0] 가로로 이동
        cursor[0] += thumb_size[0] # 맨처음 커서 위치

        if cursor[0] >= rowcols[0] * thumb_size[0]:
            cursor[1] += thumb_size[1] # cursor[1] 아래 수직으로 이동
            cursor[0] = 0  # cursor[0] 오른쪽 평행으로 이동
    return canvas


#4. 사용자가 원하는 폴더에 있는 파일 가져오는 함수
def search_dir(dirname):
    result_file_lists = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filepath = os.path.join(dirname, filename)
        if os.path.isdir(full_filepath):
            result_file_lists.extend(search_dir(full_filepath))
        else:
            # 5-1 가져온 파일의 확장자 확인
             mimetype = "" if mimetypes.guess_type(full_filepath)[0] is None else mimetypes.guess_type(full_filepath)[0]
            if mimetype.find("video1") >= 0:
                result_file_lists.append(full_filepath)
    return result_file_lists
      
#6.확장자 변경 함수 만들기
def my_imwrite(filename, img):
    try:
        ext = os.path.splitext(filename)[-1] # 확장자만 분리
        result, buffer = cv2.imencode(ext, img) # 확장자에 따라서 img파일의 확장자 인코딩
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
    new_filename = os.path.splitext(file)[0] + ".jpg" #5-2 새롭게 저장된 파일 이름 만들기
    images = get_video(file, 9)
    canvas = create_collage(images, rowcols=(3,3))
    #cv2.imwrite # imwrtie 함수는 파일명이 영어이외의 문자가 섞이면 오류발생하므로 사용불가
    my_imwrite(new_filename, canvas)
