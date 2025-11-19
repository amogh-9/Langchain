#length based text splitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader('sample.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=0,
    separator=''
)

result= splitter.split_documents(docs)
print(result[1].page_content)
