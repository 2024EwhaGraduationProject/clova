# clova-backend-PA
clova-backend-pythonanywhere

<br>
20241010 04:29 1차 actions 테스트
20241010 09:31 2차 actions 테스트
20241010 09:44 3차 actions 테스트

20241010 09:47 5차 actions 테스트
20241010 11:05 6차 actions 테스트ㄴ
20241010 11:30 7차 actions 테스트

20241010 12:06 10차 actions 테스트
20241010 12:10 11차 actions 테스트
20241010 17:25 12차 actions 테스트
20241010 17:55 13차 actions 테스트
20241010 18:01 14차 actions 테스트
20241010 18:13 15차 actions 테스트

20241013 23:13 16차 actions 테스트
20241013 23:30 17차 actions 테스트
20241013 23:33 18차 actions 테스트
20241013 23:45 19차 actions 테스트

20241014 00:04 21차 actions 테스트 : requirements.txt에 numpy 명시적으로 추가
20241014 00:16 22차 actions 테스트 : alpine to slim-buster 변경
20241014 00:23 23차 actions 테스트 : alpine to slim-buster 변경시 오류 발생가능한 패키지 삭제
20241014 00:27 24차 actions 테스트 : mysqlclient 설치 위한 pkg-config 외의 패키지 다수 추가
20241014 00:29 25차 actions 테스트 : 오류 일으키는 패키지 삭제 libmysqlclient-dev
20241014 00:40 26차 actions 테스트 : mysqlclient==2.1.1로 downgrading
20241014 00:46 27차 actions 테스트 : libmysqlclient15-dev로 다시 설치
20241014 00:49 28차 actions 테스트 : libmysqlclient15-dev에 sudo 권한 추가
20241014 00:51 29차 actions 테스트 : 앞선 패키지 대신 mysql-server 설치
20241014 00:54 30차 actions 테스트 : default-libmysqlclient-dev로 재설치
20241014 01:09 31차 actions 테스트 : libmysqlclient-dev 설치 위해 setuptools, wheel 업그레이드
20241014 01:12 32차 actions 테스트 : libmysqlclient-dev 재삭제 
20241014 01:17 33차 actions 테스트 : final의 libmysqlclient-dev 앞 sudo 삭제
20241014 01:20 34차 actions 테스트 : final의 libmysqlclient-dev 삭제
20241014 01:25 35차 actions 테스트 : final에서 default-libmysqlclient-dev로 수정, mysql 설치 추가
20241014 01:32 36차 actions 테스트 : apt-get install -y libmysqlclient21 추가
20241014 01:34 37차 actions 테스트 : final에서 mysql 설치 삭제
20241014 01:36 38차 actions 테스트 : final에서 mysql 설치 location 명시
20241014 01:36 39차 actions 테스트 : final에서 wget pip 설치
20241014 01:43 39차 actions 테스트 : final에서 lsb-release pip 설치
20241014 01:44 40차 actions 테스트 : final에서 gnupg pip 설치
20241014 01:47 41차 actions 테스트 : MySQL 레포지토리의 GPG 키 추가 코드 작성
20241014 01:49 42차 actions 테스트 : GPG 키 오류 해결 위한 코드 추가
20241014 01:51 43차 actions 테스트 : 우분투에서 GPG 키 직접 가져오는 코드 추가