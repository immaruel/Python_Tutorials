import cv2
import numpy as np # numpy의 별칭을 np로 부르겠다
import os
import mimetypes # 확장자 확인 라이브러리


# 0. 전체 컷 분리 함수
def get_video(filepath, capture_count=1):
    images = []

    # 1. 기본 동영상 정보
    cap = cv2.VideoCapture(filepath) # videoCapture 라이브러리 사용
    v_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 총 프레임수
    v_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 해상도
    v_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 해상도
    v_fps = cap.get(cv2.CAP_PROP_FPS) # 초당 프레임
    v_duration = v_frames / v_fps  # 재생속도
    #print(v_frames, v_width, v_height, v_fps, v_duration) # 734 852 480 23.999476850640857 : 총프레임수, 852 X 480 해상도, 초당 23.999476850640857프레임, 30.584s 재생시간

    # 3. 동영상 길이에 n부분에 해당하는 컷 가져오기
    jump_frame = int(v_frames / capture_count) # 몇 n부분씩 나눌지 설정

    for i in range(capture_count):
        pos = 1 + (jump_frame * i)
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos) # 캡처할 위치로 이동
        # 2. 이미지 가져오기
        ret, frame = cap.read() #ret는 cap을 ead 했는지 True Or False 한것, frame:실제 이미지
        if ret: # ret가 True면
            images.append(frame)
    cap.release()
    return images

# 4. n번만큼 분리된 컷을 한장으로 합쳐주는 함수
def create_collage(image_list,thumb_size=(210,137), rowcols=(5,5)):
    canvas_width = thumb_size[0] * rowcols[0] # 전체가로 길이
    canvas_height = thumb_size[1] * rowcols[1] # 전체세로 길이
    canvas = np.zeros(shape=(canvas_height, canvas_width, 3), dtype=np.uint8) # zeors:초기화, 3:컬러이미지이므로 3채널, 자료type은 부호없는 정수형(uint)
    canvas.fill(255)
    print(canvas)
#create_collage([])
    cursor = [0,0]
    for img in image_list:
        img = cv2.resize(img, thumb_size) # 컷분리된 사진사이즈만큼 리사이즈

        # image[y:y+height, x:x+width]
        canvas[cursor[1]:cursor[1] + thumb_size[1], cursor[0]:cursor[0] + thumb_size[0]] = img # cursor[1] 세로로 이동, cursor[0] 가로로 이동
        cursor[0] += thumb_size[0]

        if cursor[0] >= rowcols[0] * thumb_size[0]:
            cursor[1] += thumb_size[1]
            cursor[0] = 0
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
            mimetypes = "" if mimetypes.guess_type(full_filepath)[0] is None else mimetypes.guess_type(full_filepath)[0]
            if mimetype.find("video") >= 0:
                result_file_lists.append(full_filepath)
    return result_file_lists
    # 5-1 가져온 파일이 동영상(확장자)인지 확인


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
    new_filename = os.path.splitext(file)[0] + ".jpg"
    images =get_video(filepath, 9)
    canvas = create_collage(images, rowcols=(3, 3))  
    my_imwrite(new_filename, canvas)

# filepath = "c:\\test\\movie.mp4"
# images =get_video(filepath, 9)
# canvas = create_collage(images, rowcols=(3, 3))
# cv2.imshow("A",canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()