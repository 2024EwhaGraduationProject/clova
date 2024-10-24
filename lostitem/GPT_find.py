def eng_to_kor(text):
  import os

  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  json_file_path = os.path.join(BASE_DIR, 'extended-medium-423214-k4-3cd01a759605.json')

  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json_file_path 
  
  from google.cloud import translate_v2 as translate
  translate_client = translate.Client()
  if isinstance(text, bytes): text = text.decode("utf-8")
  result = translate_client.translate(text, target_language='ko')
  return result["translatedText"]
  
  
def color_word(text):
  color_dict = {
    '빨강색': '레드', '주황색': '오렌지','노랑색': '옐로우','초록색': '그린',
    '파랑색': '블루','남색': '네이비','보라색': '퍼플','분홍색': '핑크',
    '갈색': '브라운','검정색': '블랙','회색': '그레이','흰색': '화이트',
    '베이지색': '베이지','연두색': '라이트그린','민트색': '민트','하늘색': '스카이블루',
    '자주색': '마젠타','금색': '골드','은색': '실버','연핑크색': '라이트핑크',
    '연보라색': '라벤더','크림색': '크림','올리브색': '올리브','카키색': '카키','와인색': '와인'
  }
  for word in text[:]:
    if word in color_dict: text.append(color_dict[word])
  return text
  
  
def process2(text):
  import re
  #토큰화
  from konlpy.tag import Komoran
  kom=Komoran()
  #한국어 명사 추출
  x=kom.nouns(text)

  #영단어 추출 > 소문자화 및 한글 표현 추가
  eng_words = re.findall(r'\b[a-zA-Z]+\b', text)
  eng_words =[i.lower() for i in eng_words]; x+= eng_words
  loanwords = [eng_to_kor(i) for i in eng_words]; x+= loanwords

  #색깔 단어 추가
  x=color_word(x)

  #불용어 제거
  stop_words = set(['재질','브랜드','로고','텍스트','패턴','질감','색상','무늬','모양','바탕'])
  x = [word for word in x if word not in stop_words]
  return x

def similarity(result, find_prompt):
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    
    documents = [' '.join(i) for i in result]
    tfidf_vectorizer = TfidfVectorizer() # TF-IDF 벡터화
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents + [find_prompt])
    cosine_similarities = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1]) # 코사인 유사도 계산
    sorted_indices = np.argsort(cosine_similarities[0])[::-1]
    top_3_indices = sorted_indices[:3]  # 상위 3개
    return top_3_indices

# def find(df, find_prompt):
#     result = [process2(i) for i in df['description']] 
#     idx = similarity(result, find_prompt)  
#     top_lostids = df.iloc[idx]['lostid'].tolist()
#     return top_lostids

def find(data, find_prompt):
    result = [process2(i['description']) for i in data]
    idx = similarity(result, find_prompt)
    top_lostids = [data[i]['lostid'] for i in idx]
    return top_lostids

# def find_main():  # 최종 메인 함수
#     import pandas as pd
#     df = pd.DataFrame(data["data"])
#     df = df[['lostid', 'description', "category"]] #데이터 형태 아래와 같은 형식이라고 가정함
#     idx = find(df, "분홍색 스탠리 텀블러") #리턴 값이 물건의 lostid
#     print(idx)