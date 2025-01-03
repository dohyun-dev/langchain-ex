# 2-2-1 Document Locader - WebBaseLoader
"""
WebBaseLoader는 특정 웹 페이지의 내용을 로드하고 파싱하기 위해 설계된 클래스
web_paths :
매개변수는 로드할 웹 페이지의 URL을 단일 문자열 또는 여러 개의 URL을 시퀀스 배열로 지정할 수 있습니다.
여기서는 파이썬 투플(tuple) 형태로 2개의 URL을 사용하고 있습니다.

bs_kwargs :
BeautifulSoup을 사용하여 HTML을 파싱할 때 사용되는 인자들을 딕셔너리 형태로 제공합니다.
예제에서는 bs4.SoupStrainer를 사용하여 특정 클래스 이름을 가진 HTML 요소만 파싱하도록 지정하고 있습니다.
"article-header", "article-title" 클래스를 가진 요소만 선택하여 파싱합니다.
"""
import bs4
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

# 여러 개의 url 지정 가능
url1 = "https://blog.langchain.dev/customers-replit/"
url2 = "https://blog.langchain.dev/langgraph-v0-2/"

loader = WebBaseLoader(
    web_paths=(url1, url2),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("article-header", "article-content")
        )
    ),
)

docs = loader.load()

print(docs)