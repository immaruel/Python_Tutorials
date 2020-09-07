'''
내 컴퓨터의 동영상 썸네일 콜라주를 자동으로 만들어주는 프로그램
col,width -> 가로 , row,height -> 세로
'''

import cv2
import numpy as np
import os
import mimetypes # 확장자 확인 라이브러리


#2. 비디오 가져오기 함수
def get_video(filepath, capture_count=1):
    images= []
    #1. 동영상정보 받아오기
    #filepath = "c:\\test\\movie1.mp4"

    cap = cv2.VideoCapture(filepath) # videoCapture 라이브러리 사용
    v_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 총 프레임수
    v_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 가로 해상도
    v_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 세로 해상도
    v_fps = cap.get(cv2.CAP_PROP_FPS) # 초당 프레임
    v_duration = v_frames / v_fps  # 재생속도
    #print(v_frames, v_width, v_height, v_fps, v_duration) # 734 852 480 23.999476850640857 : 총프레임수, 852 X 480 해상도, 초당 23.999476850640857프레임, 30.584s 재생시간

    jump_frame = v_frames / capture_count # 총 동영상 길이 n 나누기 한 횟수설정: 몇 장을 캡처할것인지?

    for i in range(capture_count):
        pos = 1 + (jump_frame * i)
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos) # 다음 캡처쪽으로 움직일 커서
        ret,frame = cap.read()
        if ret: # ret가 True이면
            # cv2.imshow("frame",frame)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            images.append(frame)
    cap.release() # cap함수를 사용하였으면 항상 release를 끝에 해야함
    return images

#3. n번 캡처된 이미지를 합쳐주는 함수
def create_collage(image_list, thumb_size=(210,137), rowcols=(5,5)): # thumb_size(한 장의 캡처사진크기)
    canvas_width = thumb_size[0] * rowcols[0] # 전체가로 길이
    canvas_height = thumb_size[1] * rowcols[1] # 전체세로 길이
    canvas = np.zeros(shape=(canvas_height, canvas_width, 3), dtype=np.uint8) # zeors:초기화, 3:컬러이미지이므로 3채널, 자료type은 부호없는 정수형(uint)
    canvas.fill(326) # 나머지 부분은 326번에 해당하는 색으로 채우기    

    #3-1 커서가 이동하면서 다음 캡처본으로 넘어가게 채워주기
    cursor = [0,0]
    for img in image_list:
        #print(cursor)
        img = cv2.resize(img, thumb_size) # thumb_size만큼 리사이즈
        # image[y:y+height, x:x+width]
        canvas[cursor[1]:cursor[1] + thumb_size[1], cursor[0]:cursor[0] + thumb_size[0]] = img # cursor[1] 세로로 이동, cursor[0] 가로로 이동
        cursor[0] += thumb_size[0] # 맨처음 커서 위치

        if cursor[0] >= rowcols[0] * thumb_size[0]:
            cursor[1] += thumb_size[1] # cursor[1] 아래 수직으로 이동
            cursor[0] = 0  # cursor[0] 오른쪽 평행으로 이동
    return canvas

# 5. 사용자가 원하는 폴더에 있는 파일 가져오는 함수
def search_dir(dirname):
    result_file_lists = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filepath = os.path.join(dirname, filename)
        if os.path.isdir(full_filepath):
            result_file_lists.extend(search_dir(full_filepath))
        else:
            # 5-1 가져온 파일이 동영상(확장자)인지 확인
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

# filepath = "c:\\test\\movie1.mp4"
# images = get_video(filepath, 9)
# # for i in images:
# #     cv2.imshow("a",i)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
# canvas = create_collage(images, rowcols=(3,3))
# cv2.imshow("a",canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()