import ftplib
from tqdm import tqdm  # 상태바를 만들어주는 라이브러리
# 2-1. 폴더or 파일 구분하기
def is_file(ftp, filename):
    current = ftp.pwd() # 현재경로 저장
    try:
        ftp.cwd(filename)
    except:
        ftp.cwd(current)
        return True
    ftp.cwd(current)
    return False
    


FTP_SERVER ="127.0.0.1"
FTP_PORT = 6500
FTP_ID = "ftp_user"
FTP_PASS = "123456"

# 0. 기본설정
ftp = ftplib.FTP()
ftp.encoding = "euc-kr" # 한글이기에 인코딩 실시
ftp.connect(FTP_SERVER, FTP_PORT) # FTP 서버에 FTP 포트로 접속해라
print(ftp.login(FTP_ID, FTP_PASS))

# 1. 사용자 명령어 입력받는 구조 만들기
while True:
    current = ftp.pwd() # 현재 경로를 얻어오는 함수
    cmd = input("FTP {}> ".format(current)) # 사용자에게 명령어 입력받기
    args = cmd.split(" ")
    if len(args) <= 0:
        continue
    
    command= args[0]
    del args[0] # 인자값만 남기고 나머지 삭제
    
    # 1-1. 무한루프 탈출조건 만들기
    if command == "exit":
        break
    
    # 2. 폴더 목록 보기 명령 구축
    if command =="dir" or command == "ls":
        lists = ftp.nlst() # 폴더,파일,폴더목록 구하는 함수
        for l in lists:
            if is_file(ftp, l): # 파일이면 l 넘기기
                print(l)
            else: # 폴더일 경우
                print("{}{}/".format(current, l))

    elif command == "cd":
        target = args[0]  # 위에서 "cd"를 지우고 cd 다음 명령어만 남은상태
        if not is_file(ftp, target):
            ftp.cwd(target) # target으로 이동하라
    
    #3. 폴더 만드는 명령 구축
    elif command == "mkdir" or command == "mk":
        target = args[0]
        ftp.mkd(target)

    #4. 폴더 삭제하는 명령 구축
    elif command == "delete" or command == "dle":
        target = args[0]
        ftp.delete(target)
    
    #5. 업로드 하는 명령 구축
    elif command == "up":
        target = args[0]
        filename = target.split("\\")[-1] # 파일명 마지막만 남도록 분리해주기
        with open(target, "rb") as file:
            ftp.storbinary("STOR" + filename, file, 2048) # 2048(->blocksize):데이터를 전송하는 패킷의 크기를 설정

    #6. 다운로드 하는 명령 구축
    elif command == "down":
        target = args[0]
        with open(target, "wb")as file:
            size = ftp.size(ftp) # 다운로드할 파일 사이즈 재가
            with tqdm(unit='blocks', unit_scale=True, leave=True, miniters =1, desc ="DOWNLOADING!", total=size) as tq:
                def callback(data): #콜백함수는 다운로드시 무조건 들어가야함
                    tq.update(len(data)) # 데이터크기만큼 다운로드해라
                    file.write(data)
                ftp.retrbinary("RETR " + target, callback=callback)


    

ftp.close()
