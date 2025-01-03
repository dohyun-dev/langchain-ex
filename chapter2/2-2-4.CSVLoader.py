# 2-2-4 Document Locader - CSVLoader
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/한국주택금융공사_주택금융관련_지수_20160101.csv",
    encoding='cp949',
    csv_args={
        'delimiter': '\n',
    }
)
data = loader.load()
print(data)
print(len(data))