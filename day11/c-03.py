# 동적페이지 라이브러리 설치
# playwright # Selenium과 비슷한 동적 페이지 조작 라이브러리
# playwright install    # 크롬(구글회사브라우저)과 비슷한 백그라운드용 브루아저

import asyncio  # 비동기 라이브러리
from playwright.async_api import async_playwright

# 예제3] 동적 페이지 크롤링 , 대기/이벤트 존재하는 상태
# 1) 크롤링할 페이지 주소 가져온다. 파라미터 분석, ssc = 검색결과 탭 메뉴, query=검색어
url = "https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query=아야노코지"
# 2) 비동기 함수 만들기
# async def 함수명() : # 함수 선언하고 동기화

async def run():
    # 2-1) async_playwright() 실행하고 종료되기 전까지 동기화 처리
    async with async_playwright() as p:
        # 2-2) 크로미움(구글 회사 제공하는 백그라운드용 오픈소스 브라우저)
        # await.p.chromium.lauch(headless = True 백그라운드 / False 뷰모드)
        broswer = await p.chromium.launch(headless = True)
        # 2-3) 현재 실행된 크로미움의 새로운 페이지(빈 페이지) 열기
        page = await broswer.new_page()
        # 2-3) 빈 페이지에 특정한 URL 주소 대입/이동
        await page.goto(url)

        # 3) 스크롤 내리기, 2번
        for i in range(2):
            await page.wait_for_timeout(2000) # page.wait_for_timeout(밀리초): 밀리초 만큼 대기상태 함수
            # await page.evaluate("js 코드 삽입")
            # document.scrollTo(가로, 세로) : 스크롤 이동 함수
            # document.body.scrollHeight : 현재 페이지의 스크롤 세로높이
            # window.scrollTo(0, document.body.scrollHeight) : 현재 스크롤을 페이지의 가장 하단으로 이동
            await page.evaluate("document.body.scrollTo(0, document.body.scrollHeight)")

            # 4) 특정 마크업 가져오기 , .query_selector 한개 추출, query_selector_all 여러개 추출
            items = await page.query_selector_all(".tile_item._fe_image_tab_content_tile") # 이미지와 사진이름
            print(items)

            # 5) 반복문 이용한 사진/제목
            for item in items:
                title = await item.query_selector(".info_title")
                title = await title.inner_text() # 특정한 마크업의 사이 텍스트 추출(.innerText)
                img = await item.query_selector("._fe_image_tab_content_thumbnail_image")
                img = await img.get_attribute('src')
                print(title , img)

# *** asyncio.run(동기화함수()) ***
asyncio.run(run())

