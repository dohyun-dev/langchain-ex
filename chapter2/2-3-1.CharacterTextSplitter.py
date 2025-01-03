# TextSplitter - CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader(file_path="./data/history.txt", encoding="utf-8")
# text_splitter = CharacterTextSplitter(
#     separator = '',
#     chunk_size = 500,
#     chunk_overlap  = 100,
#     length_function = len,
# )
# 특정 문자열 기준으로 나누기
text_splitter = CharacterTextSplitter(
    separator = '',
    chunk_size = 500,
    chunk_overlap  = 100,
    length_function = len,
)

data = loader.load()
texts = text_splitter.split_text(data[0].page_content)
print(texts[0])

