# 예제 2] 동적페이지 크롤링 (페이징 처리)

# 예스 24 베스트 셀러 도서 정보 크롤링 / 페이징 처리(반복문)

# 1) 크롤링할 주소 가져온다. 정리/분석 , categoryNumber=001 국내도서 002 외국도서, pageNumber 페이지번호
# https://www.yes24.com/product/category/bestseller?pageNumber=1&pageSize=24&categoryNumber=001
import requests
from bs4 import BeautifulSoup

book_list = []

for page in range(1, 4):
    url = f"https://www.yes24.com/product/category/bestseller?pageNumber={page}&categoryNumber=001"
    # 2) URL 요청
    response = requests.get(url)

    # 3) HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    # 4) 특정한 마크업 추출(책제목, 가격, 저자)
    books = soup.select(".item_info")

    # 5) 여러개 추출한 마크업에서 특정한 마크업 추출, gd_name, yes_b , info_math
    for book in books :
        title = book.select_one('.gd_name').get_text()
        author = book.select_one('.info_auth').get_text().strip().replace("\n", "")
        price = book.select_one('.yes_b').get_text().strip().replace("\n", "").replace("/r", "")
        book_list.append({"제목": title, "저자": author , "가격": price})


