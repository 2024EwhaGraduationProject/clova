# clova-backend-PA
clova-backend-pythonanywhere

<br>
<br> 20241010 04:29 1차 actions 테스트
<br> 20241010 09:31 2차 actions 테스트
<br> 20241010 09:44 3차 actions 테스트

<br> 20241010 09:47 5차 actions 테스트
<br> 20241010 11:05 6차 actions 테스트ㄴ
<br> 20241010 11:30 7차 actions 테스트

<br> 20241010 12:06 10차 actions 테스트
<br> 20241010 12:10 11차 actions 테스트
<br> 20241010 17:25 12차 actions 테스트
<br> 20241010 17:55 13차 actions 테스트
<br> 20241010 18:01 14차 actions 테스트
<br> 20241010 18:13 15차 actions 테스트

<br> 20241013 23:13 16차 actions 테스트
<br> 20241013 23:30 17차 actions 테스트
<br> 20241013 23:33 18차 actions 테스트
<br> 20241013 23:45 19차 actions 테스트

<br> 20241014 00:04 21차 actions 테스트 : requirements.txt에 numpy 명시적으로 추가
<br> 20241014 00:16 22차 actions 테스트 : alpine to slim-buster 변경
<br> 20241014 00:23 23차 actions 테스트 : alpine to slim-buster 변경시 오류 발생가능한 패키지 삭제
<br> 20241014 00:27 24차 actions 테스트 : mysqlclient 설치 위한 pkg-config 외의 패키지 다수 추가
<br> 20241014 00:29 25차 actions 테스트 : 오류 일으키는 패키지 삭제 libmysqlclient-dev
<br> 20241014 00:40 26차 actions 테스트 : mysqlclient==2.1.1로 downgrading
<br> 20241014 00:46 27차 actions 테스트 : libmysqlclient15-dev로 다시 설치
<br> 20241014 00:49 28차 actions 테스트 : libmysqlclient15-dev에 sudo 권한 추가
<br> 20241014 00:51 29차 actions 테스트 : 앞선 패키지 대신 mysql-server 설치
<br> 20241014 00:54 30차 actions 테스트 : default-libmysqlclient-dev로 재설치
<br> 20241014 01:09 31차 actions 테스트 : libmysqlclient-dev 설치 위해 setuptools, wheel 업그레이드
<br> 20241014 01:12 32차 actions 테스트 : libmysqlclient-dev 재삭제 
<br> 20241014 01:17 33차 actions 테스트 : final의 libmysqlclient-dev 앞 sudo 삭제
<br> 20241014 01:20 34차 actions 테스트 : final의 libmysqlclient-dev 삭제
<br> 20241014 01:25 35차 actions 테스트 : final에서 default-libmysqlclient-dev로 수정, mysql 설치 추가
<br> 20241014 01:32 36차 actions 테스트 : apt-get install -y libmysqlclient21 추가
<br> 20241014 01:34 37차 actions 테스트 : final에서 mysql 설치 삭제
<br> 20241014 01:36 38차 actions 테스트 : final에서 mysql 설치 location 명시
<br> 20241014 01:36 39차 actions 테스트 : final에서 wget pip 설치
<br> 20241014 01:43 39차 actions 테스트 : final에서 lsb-release pip 설치
<br> 20241014 01:44 40차 actions 테스트 : final에서 gnupg pip 설치
<br> 20241014 01:47 41차 actions 테스트 : MySQL 레포지토리의 GPG 키 추가 코드 작성
<br> 20241014 01:49 42차 actions 테스트 : GPG 키 오류 해결 위한 코드 추가
<br> 20241014 01:51 43차 actions 테스트 : 우분투에서 GPG 키 직접 가져오는 코드 추가
<br> 20241014 01:53 44차 actions 테스트 : wheels 에서 wheel로 패키지명 수정
<br> 20241014 01:58 45차 actions 테스트 : libmysqlclient-dev 설치 오류 해결 위해 임의로 저장소 추가
<br> 20241014 02:00 46차 actions 테스트 : GPG 키 오류 해결 위해 44차 테스트 코드로 복귀

<br> 20241014 12:52 47차 actions 테스트 : apt update 추가 + pkg-config 설치 위치 변경
<br> 20241014 12:55 48차 actions 테스트 : apt update 앞에 && 없던 오류 수정
<br> 20241014 12:55 49차 actions 테스트 : gcc install 추가
<br> 20241014 13:05 50차 actions 테스트 : wheels 폴더 이름명 변경 (오류)
<br> 20241014 13:08 51차 actions 테스트 : -virtual 옵션 오류나서 삭제
<br> 20241014 13:12 52차 actions 테스트 : --no-cache 옵션 오류나서 삭제
<br> 20241014 13:21 53차 actions 테스트 : 49차 테스트 코드로 복귀 + wheels 폴더 이름명 변경