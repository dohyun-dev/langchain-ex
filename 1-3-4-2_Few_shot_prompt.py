# Few-shot Prompt

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import FewShotPromptTemplate, ChatPromptTemplate, \
    HumanMessagePromptTemplate, AIMessagePromptTemplate, SystemMessagePromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# 예제 정의
examples = [
    {"input": "지구의 대기 중 가장 많은 비율을 차지하는 기체는 무엇인가요?", "output": "질소입니다."},
    {"input": "광합성에 필요한 주요 요소들은 무엇인가요?", "output": "빛, 이산화탄소, 물입니다."},
]

# 예제 프롬프트 템플릿 정의
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

# Few-shot 프롬프트 템플릿 생성
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

# 최종 프롬프트 템플릿 생성
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 과학과 수학에 대해 잘 아는 교육자입니다."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

# 모델과 체인 생성
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
chain = final_prompt | model

# 모델에 질문하기
result = chain.invoke({"input": "지구의 자전 주기는 얼마인가요?"})
print(result.content)


from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

# 더 많은 예제 추가
examples = [
    {"input": "지구의 대기 중 가장 많은 비율을 차지하는 기체는 무엇인가요?", "output": "질소입니다."},
    {"input": "광합성에 필요한 주요 요소들은 무엇인가요?", "output": "빛, 이산화탄소, 물입니다."},
    {"input": "피타고라스 정리를 설명해주세요.", "output": "직각삼각형에서 빗변의 제곱은 다른 두 변의 제곱의 합과 같습니다."},
    {"input": "DNA의 기본 구조를 간단히 설명해주세요.", "output": "DNA는 이중 나선 구조를 가진 핵산입니다."},
    {"input": "원주율(π)의 정의는 무엇인가요?", "output": "원의 둘레와 지름의 비율입니다."},
]

# 벡터 저장소 생성
to_vectorize = [" ".join(example.values()) for example in examples]
embeddings = OpenAIEmbeddings()
vectorstore = InMemoryVectorStore.from_texts(to_vectorize, embeddings, metadatas=examples)

# 예제 선택기 생성
example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=2,
)

# Few-shot 프롬프트 템플릿 생성
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_selector=example_selector,
    example_prompt=ChatPromptTemplate.from_messages(
        [("human", "{input}"), ("ai", "{output}")]
    ),
)

# 최종 프롬프트 템플릿 생성
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 과학과 수학에 대해 잘 아는 교육자입니다."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

# 모델과 체인 생성
chain = final_prompt | ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

# 모델에 질문하기
result = chain.invoke("태양계에서 가장 큰 행성은 무엇인가요?")
print(result.content)
