# 2-2-3 Document Locader - Directory Loader
"""
DirectoryLoader를 사용하여 디렉토리 내의 모든 문서를 로드할 수 있습니다. DirectoryLoader 인스턴스를 생성할 때 문서가 있는 디렉토리의 경로와 해당 문서를 식별할 수 있는 glob 패턴을 지정합니다.
이 때 문서를 읽고 처리하기 위해서 UnstructuredLoader 가 내부적으로 사용됩니다. PDF, XML, HTML 등 미리 정의된 형식이 없는 텍스트 문서를 전처리하고 구조화된 형식으로 변환합니다. 이 로더를 사용하려면 unstructured 라이브러리가 설치되어 있어야 합니다.
"""
from idlelib.iomenu import encoding

from langchain_community.document_loaders import DirectoryLoader, TextLoader

"""
모든 .txt 파일을 찾는 작업을 하려면 다음과 같이 glob 모듈과 os.path.join 함수를 사용할 수 있습니다.
"""
import os
from glob import glob

files = glob(os.path.join('./data', '*.txt'))
print(files)

loader = DirectoryLoader(path="./data", glob="*.txt", loader_cls=TextLoader, loader_kwargs={"encoding":"utf-8"})
data = loader.load()
print(data)