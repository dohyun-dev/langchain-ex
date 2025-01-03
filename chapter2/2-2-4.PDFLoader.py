from langchain_community.document_loaders import PyPDFLoader, UnstructuredPDFLoader

pdf_filepath = './data/000660_SK_2023.pdf'

loader = PyPDFLoader(pdf_filepath)
pages = loader.load()

print(len(pages))
print(pages)

print("====")


# 전체 텍스트를 단일 문서 객체로 변환
loader = UnstructuredPDFLoader(pdf_filepath)
pages = loader.load()

print(len(pages))