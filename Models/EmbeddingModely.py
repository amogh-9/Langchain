from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
model = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

vector = model.embed_query("hello world!")
print(vector)
