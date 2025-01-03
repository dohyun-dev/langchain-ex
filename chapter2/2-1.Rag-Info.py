# Rag Info (Rag 개요)

"""
RAG 파이프 라인은
데이터 로드 -> 텍스트 분할 -> 인덱싱 -> 검색 -> 생성 으로 구성
Data Load -> Split -> indexing -> Retriever -> Create
"""
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# 1. 데이터 로드
# Data Loader - 웹페이지
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 위키피디아 정책과 지침
url = 'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EC%A0%95%EC%B1%85%EA%B3%BC_%EC%A7%80%EC%B9%A8'
loader = WebBaseLoader(url)

# 웹페이지 텍스트 -> Documents
docs = loader.load()

print(len(docs))
print(len(docs[0].page_content))
print(docs[0].page_content[5000:6000])

# 2. 텍스트 분할
# Text Split (Documents -> Small chunks : Doucments)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

print(len(splits))
print(splits[10].page_content)
print(splits[10].metadata)

# 3. 인덱싱
# Indexing (Texts -> Embedding -> Store)
from langchain_core.vectorstores import InMemoryVectorStore

vector_store = InMemoryVectorStore(embedding=OpenAIEmbeddings())
vector_store.add_documents(splits)


# 4. 검색
docs = vector_store.search("격하 과정에 대해서 설명해주세요.", search_type="similarity")
print(len(docs))
print(docs[0].page_content)

# 4. 생성
"""
검색된 정보를 바탕으로 사용자의 질문에 답변을 생성하는 최종 단계입니다. 
LLM 모델에 검색 결과와 함께 사용자의 입력을 전달합니다. 
모델은 사전 학습된 지식과 검색 결과를 결합하여 주어진 질문에 가장 적절한 답변을 생성합니다.
"""

prompt = ChatPromptTemplate.from_messages([HumanMessagePromptTemplate.from_template(
    """
    Answer the question based only on the following context {context}            
    Question: {question}
    """)
])

model = ChatOpenAI(
    model="gpt-4o-mini",

)

retriever = vector_store.as_retriever()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
        {'context': retriever | format_docs, 'question': RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
)

print("==== 결과 ===")
print(rag_chain.invoke("격하 과정에 대해서 설명해주세요."))