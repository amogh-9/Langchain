#Text Loader
from langchain_community.document_loaders import TextLoader
loader = TextLoader('file_path.txt')
doc = loader.load()
print(doc[0].page_content)  #load createsa document object that has metadata and page_content field(actual data)

#PDF loader
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('file.pdf')
docs = loader.load()
print(docs[0].page_content) #loads each pdf page in a separate document object

#load vs lazy_load()
#load puts all the doc objects into memory where as lazy_load only puts the object into memory when it is called or iterated through

#webBase loader
from langchian_community.document_loaders import WebBaseLoader
url='website-link;
loader=WebBaseLoader(url)
docs=loader.load() #loads text content of website
#WebBaseLoader extracts html content , for website with heavy js use ->SeleniumURLLoader 

#CSVLoader
from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(file_path='Social_Network_Ads.csv')
docs = loader.load() #loads each row as separate doc object
