# 2-2-2 Document Locader - Text Loader
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

loader = TextLoader('data/history.txt', encoding='utf-8')
data = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size= 100, chunk_overlap=20)
docs = splitter.split_documents(data)
vector_store = InMemoryVectorStore(embedding=OpenAIEmbeddings())
vector_store.add_documents(docs)
retriever = vector_store.as_retriever()

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("당신은 역사를 가르쳐 주는 역사 선생님입니다. 반말로 정중하게 질문에 대한 답변을 해주세요."),
        HumanMessagePromptTemplate.from_template("""
        주어진 정보를 통해서 답변해주세요.
        주어진 정보 : {context}
        질문 : {question}    
        """)
    ]
)

model = ChatOpenAI(model="gpt-4o-mini")
chain = ({"context" : retriever, "question": RunnablePassthrough()} | prompt | model | StrOutputParser())
print(chain.invoke("고조선은 언제 세워졌나요?"))
