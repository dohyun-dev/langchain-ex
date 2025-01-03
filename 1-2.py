from itertools import chain

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# 1. 컴포넌트 정의
prompt1 = ChatPromptTemplate.from_template("지구과학에서 {topic}에 대해 간단히 설명해주세요.")
model = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()
#
# # 2. 체인 생성
chain = prompt1 | model | output_parser
#
# # 3. LLM 호출
# response = chain.invoke({"topic": "마그마"})


# # batch 메소드
# topics = ["지구 공전", "화산 활동", "대륙 이동"]
#
# results = chain.batch([{"topic": t} for t in topics])
#
# for topic, result in zip(topics, results):
#     print(f"{topic} 설명: {result}")


# stream 메소드
stream = chain.stream({"topic": "지진"})
print("stream 결과:")
for chunk in stream:
    print(chunk, end="", flush=True)