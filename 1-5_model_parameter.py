# model parameter

"""
Temperature: 생성된 텍스트의 다양성을 조정합니다. 값이 작으면 예측 가능하고 일관된 출력을 생성하는 반면, 값이 크면 다양하고 예측하기 어려운 출력을 생성합니다.
Max Tokens (최대 토큰 수): 생성할 최대 토큰 수를 지정합니다. 생성할 텍스트의 길이를 제한합니다.
Top P (Top Probability): 생성 과정에서 특정 확률 분포 내에서 상위 P% 토큰만을 고려하는 방식입니다. 이는 출력의 다양성을 조정하는 데 도움이 됩니다.
Frequency Penalty (빈도 패널티): 값이 클수록 이미 등장한 단어나 구절이 다시 등장할 확률을 감소시킵니다. 이를 통해 반복을 줄이고 텍스트의 다양성을 증가시킬 수 있습니다. (0~1)
Presence Penalty (존재 패널티): 텍스트 내에서 단어의 존재 유무에 따라 그 단어의 선택 확률을 조정합니다. 값이 클수록 아직 텍스트에 등장하지 않은 새로운 단어의 사용이 장려됩니다. (0~1)
Stop Sequences (정지 시퀀스): 특정 단어나 구절이 등장할 경우 생성을 멈추도록 설정합니다. 이는 출력을 특정 포인트에서 종료하고자 할 때 사용됩니다.
"""
from langchain_openai import ChatOpenAI

ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5, # 생성된 텍스트의 다양성 조정
    max_tokens=100, # 최대 토큰수
    top_P=0.5, # 상위 P% 토큰만을 고려
    frequency_penalty=0.5, # 이미 등장한 단어의 재등장 확률
    presence_penalty=0.5, # 새로운 단어의 도입을 장려
    stop=["\n"] # 정지 시퀀스
)