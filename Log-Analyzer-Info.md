1.`112.171.112.201`   
: 호출된 인터넷 IP

2.`http-nio-80-exec-664`  
: 쓰레드 NAME

3.`-(%l)`

: 출력에서 "빼기기호"는 요청한 정보가 없음을 나타낸다. 이 경우 여기에 나올 정보는 클라이언트 컴퓨터의 `identd`가 제공할 클라이언트의 RFC 1413 신원이다. 이 정보는 매우 믿을 수 없기때문에, 긴밀히 관리되는 내부 네트웍이 아니라면 절대로 이 정보를 사용하면 안된다. `IdentityCheck`가 `On`이 아니라면 아파치 웹서버는 이 정보를 알아보려고 시도하지도 않는다.

4.`sohnhyeok@giftm.co.kr`  
: USERID  

5. `[24/Aug/2018:00:00:01 +0900]`
: TIME  
[10/Oct/2000:13:55:36 -0700] (%t)
서버가 요청처리를 마친 시간. 형식은:
[day/month/year:hour:minute:second zone]
day = 숫자 2개
month = 숫자 3개
year = 숫자 4개
hour = 숫자 2개
minute = 숫자 2개
second = 숫자 2개
zone = (`+' | `-') 숫자 4개

로그 형식문자열에 %{format}t를 사용하여 다른 형식으로 시간을 출력할 수 있다. format은 C 표준 라이브러리의 strftime(3)과 같다.

6.`GET`  
: REST method

7.`/api/ehr/attnd/record`   
: REST API

8.`HTTP/1.1`  
HTTP VERSION

9.`200`   
KNOWN NUMBER

10.`888`   
패킷 사이즈

11.`"https://giftm.daouoffice.com/app/home"`  
: Base_URL

12.` "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"` 
: User-Agent

13.`"-"`  
:만약 USER-AGNET가 없을 경우에 백업용으로 사용됨.

14.`0.093`  
: taking time