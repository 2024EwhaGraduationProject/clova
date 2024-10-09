def gpt_conn():
    from dotenv import load_dotenv
    import os
    import openai
    from openai import OpenAI

    load_dotenv()  # .env 파일 로드
    openai.api_key = os.getenv('chatGPT_API')
    client = OpenAI(api_key=openai.api_key)
    return client

def encode_image_to_base64(image_path):
    #이미지 파일을 base64로 인코딩하는 함수
    import base64
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')

def gpt_result(image_path,prompt,client):
    #이미지 파일을 받아 GPT 모델로부터 결과를 반환하는 함수
    ex_url='https://url.kr/frss41'

    # 이미지를 base64로 인코딩
    base64_image = encode_image_to_base64(image_path)

    # GPT 모델 호출
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role": "system", "content": prompt},

          {"role": "user",
              "content": [
                  { "type": "image_url", "image_url": { "url": ex_url,} }, ],
          },
          {"role": "assistant", "content": "우산 : 흰색 천과 검정색 손잡이를 가진 우산입니다. 흰색 우산"},

          {"role": "user",
                "content": [
                    { "type": "image_url", "image_url": f"data:image/png;base64,{base64_image}" },
                ],
          },
                ],

        seed=1886, temperature=0.4,
    )
    return chat_completion.choices

def process1(x):
    lines = x.split('\n')
    result2 = [line.split(':', 1)[1].strip() for line in lines]
    cat = result2[0] ; desc=result2[1]; title = result2[2]
    return cat, desc, title

def register(file):
  import random
  random.seed(1886)

  set_prompt = (
    "당신은 분실물 정보를 객관적이고 이성적인 시각으로 입력하는 직원입니다. "
    "분실물의 사진을 보고, 다음과 같은 형식으로 응답을 작성하십시오: "
    "1. 카테고리: [물건의 카테고리] "
    "2. 특징: [발견할 수 있는 모든 특징을 활용해 작성한 자연스러운 한 문장] "
    "3. 제목: [해당 물건을 대표할 제목] "
    "카테고리는 텀블러, 우산, 충전기/케이블선, 이어폰/헤드셋, 생활용품, 전자제품, 개인정보 포함 물품, 서적/문구류, 패션/악세서리/인형/화장품, 지갑, 기타 중에서 선택하십시오. "
    "특징 정보에는 물품의 이름, 색깔, 재질, 패턴, 텍스트, 브랜드 이름, 로고 등에서 발견한 모든 요소를 언급해야 합니다. "
    "포스트잇에 쓰여진 텍스트는 무시해도 되며, 신용카드, 사람이 포함된 사진, 서류 등은 '개인정보 포함 물품' 카테고리로 선택하십시오. "
    "사진 속에 물체가 여러 개 있다면, 각각에 대해 이 형식으로 작성하십시오."
    "색깔은 빨강색, 주황색, 노랑색, 초록색, 파랑색, 남색, 보라색, 분홍색, 갈색, 검정색, 회색, 흰색, 베이지색, 민트색, 연두색, 자주색, 금색, 은색, 연핑크색, 연보라색, 크림색, 올리브색, 카키색, 와인색 중에서 선택하십시오. "
    )

  result = gpt_result(file,set_prompt,gpt_conn())[0].message.content
  cat, desc, title = process1(result)
  return cat, desc, title

################################### 최종 실행코드 하단
# import requests
# url = 'https://www.hydroflask.com/media/catalog/product/cache/77db0a5f883b6795ccfad0b5f4e74aee/t/2/t20cpb504-20-oz-all-around-tumbler-press-in-lid-moonshadow-straight_1.jpg'
# response = requests.get(url)
# with open('ex1.jpg', 'wb') as file: file.write(response.content)

# import time; time.sleep(1)
# file= './ex1.jpg'
# cat, desc, title= register(file) # 리턴 값
# print(cat, desc, title)