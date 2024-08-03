from bs4 import BeautifulSoup
import requests

# 블로그 메인 페이지의 HTML 가져오기
html_code = requests.get("https://blog.naver.com/skfoodcompany").text
soup = BeautifulSoup(html_code, 'html.parser')

# 첫 번째 iframe의 src URL 추출
iframe = soup.find("iframe", id="mainFrame")
if iframe is not None:
    iframe_src = iframe['src']
    iframe_url = f"https://blog.naver.com{iframe_src}"

    # iframe URL을 통해 실제 블로그 게시물 페이지의 HTML 가져오기
    iframe_html_code = requests.get(iframe_url).text
    iframe_soup = BeautifulSoup(iframe_html_code, 'html.parser')

    # 모든 이미지 태그를 선택
    img_tags = iframe_soup.find_all('img')

    # 특정 패턴에 맞는 이미지 URL만 출력
    for img in img_tags:
        img_url = img.get('data-lazy-src')  # data-lazy-src 속성에서 이미지 URL 추출
        if img_url and img_url.startswith("https://postfiles.pstatic.net/"):
            print("이미지 URL:", img_url)
            break
else:
    print("iframe을 찾을 수 없습니다.")


