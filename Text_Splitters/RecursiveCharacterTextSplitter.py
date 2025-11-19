#it ries to keep the structure of original text so meaningful chunks are made
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
)

chunks = splitter.split_documents(text)
