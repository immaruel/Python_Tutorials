from myclass import MyImage #파이썬 파일, 그 파일에서 만든 class명
import argparse

p = argparse.ArgumentParser()
p.add_argument("-f", type=str)
p.add_argument("-e", type=str) # 확장자
p.add_argument("-r", action="store_true") # 리사이징
p.add_argument("-rw", type=int, default=500) # 가로 리사이징
p.add_argument("-rh", type=int, default=500) # 세로 리사이징
args = p.parse_args()

if args.f and (args.e or args.r):
    myimg = MyImage(folder=args.f,
                    ext = args.e,
                    resize= args.r,
                    r_width = args.rw,
                    r_height = args.rh)
    cnt_resize, cnt_ext = myimg.start()
    print("리사이즈: {}, 포맷변경: {}".format(cnt_resize,cnt_ext))
else:
    print("사용법: python main.py -f <대상폴더> -e <변경될 확장자> -r [리사이즈] -rw 500 -rh 500")
