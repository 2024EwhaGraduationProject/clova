# 팀 09 보성말차, 백엔드 & AI 기술 코드 설명


## 1️⃣ 폴더 구조

| 폴더 구조 | 기능 설명 |
|----|----|
| ![image](https://github.com/user-attachments/assets/630efcf9-eac7-4420-beeb-948e5ded4965) | 🚩 accounts : 계정정보, 이화인 회원가입 관련 <br><br> 🚩 clova : 설정 파일 (기본폴더) <br><br> 🚩 informations : 개인정보 및 행운포인트상점, 공지사항 등 관리 <br><br> 🚩 lostitem : 검색, 등록 등 핵심 기능 포함 |

<br><br>

## 2️⃣ 주요 코드 소개

| 주요 코드 | Source Code | 코드 설명 |
|----|----|----|
| 이화인 인증 메일 | ![image](https://github.com/user-attachments/assets/3b248fc4-fcaf-4a18-819a-143c8f184e1e) | 🚩  Django.core.mail에서 기본으로 제공하는 이메일 발송 함수를 이용하여 이화여대 이메일 인증 기능 사용 <br><br> 🚩 email 아이디만 입력받아 [ewha.ac.kr](http://ewha.ac.kr) 주소를 붙여 메일을 발송하기 때문에, 강제로 이화인 이메일로만 인증번호를 받을 수 있도록 설계 |
| 검색 기능 | 📁clova/lostitem/views.py <br> 📑LostSearchView <br><br> 📁clova/lostitem/GPT_find.py <br> ▸ 👩‍💻 사용한 오픈소스 : Google Cloud API, KoNLPy의 Komoran 형태소 분석기, scikitlearn의 TfidfVectorizer | 🚩 검색을 위해 입력 받은 정보 중 일부는 초기 필터링에 사용 <br><br> 🚩 필터링 된 DB를 가지고 **find(filtered_data, description) 함수**를 실행. find 함수는 코사인 유사도를 통해 계산된 상위 3개의 결과를 반환 <br><br> 🚩 jupyter 형식으로 작성된 코드를 .py 형식으로 수정하여 GPT_find.py 파일에 저장 후 LostSearchView에서 사용할 수 있도록 import 해오는 방식으로 설계 |
| 등록 기능 | 📁clova/lostitem/views.py <br> 📑LostImageUploadView & LostUploadView <br><br> 📁clova/lostitem/GPT_desc.py <br> ▸ 👩‍💻 사용한 오픈소스 : chat gpt 4.o API | 🚩 사용자가 입력한 사진 파일을 링크형식으로 불러오기 위해 임시로 media 파일에 저장하여, url을 불러오도록 설계 <br><br> 🚩 분실시간과 날짜는 현재 시점을 기준으로 자동으로 입력되도록 반환 <br><br> 🚩 register(imagefile) 함수를 거쳐 category, description, title 항목을 반환하도록 설계 <br><br> 🚩 register 함수는 앞선 검색 과정과 동일하게 GPT_desc.py 파일에 프롬프팅된 GPT api 함수를 작성해둔 뒤 import 하는 방식으로 구현 <br><br> 🚩 성공적으로 GPT에서 설명이 생성되었다면 서버코드 200을 반환하고 프론트엔드에 Response 응답 반환 <br><br> 🚩 GPT에서 설명이 생성되지 않았다면 error 코드를 반환하고 서버오류 500 반환하여 사용자가 프론트엔드에서 다시 이미지를 입력할 수 있도록 설계  |

<br><br>

## 3️⃣ 배포 과정에서의 추가적인 Error Handling

### 📢 Git Action 자동화를 통해 수정된 코드 자동 반영
```
git remote -v #현재 개발환경과 연결된 git remote 주소 확인
git branch -a #현재 개발환경과 연결된 git branch 이름 확인

## 수정된 code를 git에 반영하기 위한 환경이 확인된 경우 

git add .  #수정된 code 전체를 git에 올리기 위해 반영
git commit -m "commit message" #커밋 메세지를 추가하여 기능별로 update
git pull origin main #origin(local)에서 main(git)으로 반영한 코드 pull
```
- git pull 업로드된 코드는 git action을 통해 자동으로 배포 반영

- Git에 업로드하는 과정에서 chatGPT API Key, Django Key 등 민감한 정보는 .env.prod와 .env 파일에 작성하여 gitignore (GitHub에 업로드되지 않도록 관리)
- 프로젝트 빌드과정에서 꼭 필요한 비밀 정보들은 Git Secret에 작성
- git action 자동화 빌드 과정에서 필요한 파일을 임의로 생성하도록 관리

<br>

```
#(예) .github/workflows/deploy.yml

- name: create env file
  run: |
    touch .env
    echo "${{ secrets.ENV_VARS }}" >> .env
    
    #django key, Debug 여부 등이 저장된 ENV_VARS secret을 .env 파일로 빌드
    
- name: create json file
  uses: jsdaniell/create-json@v1.2.2
  with:
    name: "extended-medium-423214-k4-3cd01a759605.json"
    json: ${{ secrets.CHATGPT }}
    dir: '.'
    
    #chatGPT 실행을 위해 필요한 JSON 파일을 생성
```

<br>

### 📢 [Docker Container]
- [clova.site](http://clova.site) 내부에서 chatGPT API 실행과 검색 과정에서의 형태소 분석을 위해 무거운 dependencies가 필요
    → 이미 dependencies가 설치된 python:3.8-slim-buster를 builder로 선택하여 빌드 과정에서 time out 되지 않도록 설계
    
- Docker Container를 통해 가상환경을 구축하여 docker 위에서 웹이 작동하도록 웹 설계
```
# pull official base image
FROM python:3.8-slim-buster as builder

# set work directory
WORKDIR /usr/src/app
```
- requirements.txt에 필요한 dependencies 모두 작성하여 하나씩 설치하되, no cache dir 옵션 사용하여 설치 과정에서의 오류 최소화

```
# update pip
RUN pip install --upgrade pip

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
```

- web 빌드 과정에서 gunicorn 사용하였으나, timeout 120 옵션을 걸어 무거운 application이 설치되는 과정에서 time out 되는 것을 방지

```
 web:
    container_name: web
    build:
      context: ./
      dockerfile: Dockerfile.prod
    command: gunicorn --timeout 120 clova.wsgi:application --bind 0.0.0.0:8000
    environment:
      DJANGO_SETTINGS_MODULE: clova.settings.prod 
    env_file:
      - .env
    volumes:
      - static:/home/app/web/static
      - media:/home/app/web/media
    expose:
      - 8000
    entrypoint:
      - sh
      - config/docker/entrypoint.prod.sh
```

### 📢 [프론트-백엔드 연결 과정 요약]

1. 가비아 도메인 구매
2. AWS EC2 인스턴스 생성
3. SSH 인증서 발급 통해 https 접근 권한 허가
4. 구매한 도메인 주소 분리 [api.clova.site](http://api.clova.site) & www.clova.site
5. 프론트엔드 Vercel의 API 요청이 api.clova.site를 통해 들어오면 처리 후 [www.clova.site](http://www.clova.site)로 결과 반환하도록 도메인 설정

### 📢 [프론트-백엔드 연결 과정 자세히]

그로쓰 09팀 보성말차-이정은 기술 블로그에 자세한 연결과정을 업로드

[https://dulbong.tistory.com/entry/졸업프로젝트-AWS-Vercel-간-연결을-위한-ACM-Route53-사용](https://dulbong.tistory.com/entry/%EC%A1%B8%EC%97%85%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-AWS-Vercel-%EA%B0%84-%EC%97%B0%EA%B2%B0%EC%9D%84-%EC%9C%84%ED%95%9C-ACM-Route53-%EC%82%AC%EC%9A%A9)

<br><br>

## 4️⃣ How To Test


👇👇👇 배포 링크 접속 👇👇👇 

https://www.clova.site
