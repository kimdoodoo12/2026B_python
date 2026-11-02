# 웹 크롤링

# 파이썬 크롤링 라이브러리 : 
    # 정적(request/BeautifulSoup)
    # 동적(Selenium, Playwright)

# 확인
    # 1. 크롤링할 페이지의 도메인주소/robots.txt 접속하여 크롤링 허용 여부 확인
    # User-agent: 사용자/브라우저/AI, Disasllow: 불가능 , Allow 가능
    # 개발자도구(F12) -> 크롤링 요소 선택 -> 선택자/식별자 확인

# 필요한 라이브러리: requests, BeautifulSoup

# 1] 네이버 검색 정보 
# 1. 크롤링 주소 가져오기
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=안양날씨"
# 2. requests 라이브러리로 해당 주소 요청하기
import requests

response = requests.get(url)    # requests.get("요청할 주소")
print(response) # <Response [200]> # HTTP CODE : 200 (통신 성공 뜻)
print(response.text) # 요청할 주소의 HTML 문자로 반환

# 3. 요청 성공했으면 요청한 페이지의 HTML 파싱하기
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

# 4. 파싱한 이유 : 특정한 식별자(마크업)의 텍스트/정보 추출
# soup.select(선택자) : 여러개 추출    # soup.select_one(선택자) : 한개 추출
text = soup.select_one(".temperature_text")
print(text) # <div class="temperature_text"> <strong><span class="blind">현재 온도</span>15.2<span class="celsius">°</span></strong> </div>

# 5. 마크업 사이의 텍스트 추출
print(text.get_text())
# 추출한 DOM.get_text()

