<크롤링을 위한 사전지식>
1. HTML 태그
2. 기본적인 웹 로직
3. 브라우저의 개발자 도구 사용법 

<네트워크 프로그래밍>
- 서로 다른 원격지의 컴퓨터끼리 일련의 데이터를 주고 받을 수 있는 기능이 포함된 프로그램을 만드는 것

<소켓>
- 컴퓨터 네트워크를 경유하는 프로세스 간 통신의 종착점을 말한다.
- 소켓은 파일입출력을 네트워크로 확장시킨 추상적인 개념
- 네트워크 통신을 하는 모든 프로그램은 소켓을 생성하고 생성된 소켓을 통해서 데이터를 주고 받는다.
= 일반적인 컴퓨터의 소켓 통신은 TCP/IP, UDP/IP 프로트콜을 사용한다.

<프로토콜>
- 원거리의 컴퓨터 혹은 통신 장비 사이에 메세지를 주고 받는 양식 혹은 규칙을 말한다.
-그냥 쉽게 컴퓨터(통신기기)끼리 무언가를 주고 받기 위한 약속

- http, https, FTP, SMTP, WiFi(IEEE 802.XXX), 블루투스 등 

<세션 session>
- 정보가 서버에 저장됨

<쿠키 cookie>
- 정보가 내 컴퓨터에 저장됨

<크롤링 하는 순서>
1. 원하는 웹페이지의 접속하여 html 데이터를 받아온다.
2. 받아온 html 데이터를 분석한 가능한 형태로 가공한다.
3. 원하는 데이터를 추출한다. 

<라이브러리>

- 라이브러리 설치 : pip install 패키지명
- 라이브러리 삭제 : pip uninstall 패키지명
- 컴퓨터에 설치된 라이브러리 목록 보기 : pip freeze
- 설치된 라이브러리 정보 : pip show 패키지명
- 원하는 웹페이지의 접속하여 html 데이터를 받아오기 : pip install request
- 받아온 html 데이터를 분석한 가능한 형태로 가공 : (pip install BeautifulSoup4) or (pip install requests_html)
- 엑셀로 크롤링 결과값 받기 : pip install openpyxl + pip install pandas
- 깔끔하게 결과값을 출력시켜주는 내부 라이브러리 : pprint
- 텔레그렘 라이브러리 : pip install telepot
- pillow 라이브러리 : pip install pillow
- openCV 라이브러리 : pip install opencv-python
- scikit이미지 라이브러러리 : pip install scikit-image
- scipy 라이브러리 : pip install scipy

<이름 지정>
- 클래스(class) -> li.
- 아이디(id) -> li#

<코드 자동정렬>
ctrl + K + F