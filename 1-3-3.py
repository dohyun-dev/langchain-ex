# 챗 프롬프트 템플릿
"""
SystemMessage: 시스템의 기능을 설명합니다.
HumanMessage: 사용자의 질문을 나타냅니다.
AIMessage: AI 모델의 응답을 제공합니다.
FunctionMessage: 특정 함수 호출의 결과를 나타냅니다.
ToolMessage: 도구 호출의 결과를 나타냅니다.
"""
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system", "이 시스템은 천문학 질문에 답변할 수 있습니다."),
#     ("user", "{user_input}")
# ])

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("이 시스템은 천문학 질문에 답변할 수 있습니다."),
    HumanMessagePromptTemplate.from_template("{user_input}"),
])

print(chat_prompt.format_messages(user_input="태양계에서 가장 큰 행성은 무엇인가요?"))

model = ChatOpenAI(model="gpt-4o-mini")

chain = chat_prompt | model | StrOutputParser()

print(chain.invoke({"user_input": "태양계에서 가장 큰 행성은 무엇인가요?"}))
