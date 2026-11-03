# httpsx란? 외부 api 통신하는 라이브러리, API 연동 / SPRING API
# 라이브러리 httpx , xmltodict
# xmltodict란? httpx 라이브러리에는 .json() 타입변환 하지만 xml 변환 지원하지 않는다.
# xml 파싱

import httpx
import xmltodict
import pandas as pd
# 0] 공공데이터포털 본인 인증키
service_key = "7540ef37d4d62e8aa1ccaf9c61bc9095638232be0930450a4a0d128c78e9e7d6"

# 1] 공공데이터에 json 형식의 자료 요청, 대구광역시 중구 맛집 현황
def test1():
    # 2] 신청한 API의 주소 및 파라미터 분석, page 현재페이지, perPage = 페이지당자료수 , serviceKey
    # https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553?page=1&perPage=10&serviceKey=7540ef37d4d62e8aa1ccaf9c61bc9095638232be0930450a4a0d128c78e9e7d6
    url="https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553"
    url+= "?page=1"
    url+= "&perPage=147"
    url+= f"&serviceKey={service_key}"

    # 3} httpx이용하여 통신하기 , import httpx
    # httpx.HTTP메소드명(통신할 주소)
    response = httpx.get(url)
    # print(response)
    # 4] 응답 결과 json 변환, .json()
    response_json = response.json()
    # print(response_json)
    # 5] 판다스에 저장하기
    df = pd.DataFrame(response_json['data'])
    df.info()


# 2] 공공데이터 포털 xml 형식의 자료 요청


test1()