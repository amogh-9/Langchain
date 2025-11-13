from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash)

chat_template = ChatPromptTemplate([
  'system','You are an experienced {profession}',
  MessagePlaceholder(variable_name = 'chat_history')
  'human', 'Give me 2 line explanation about {topic}'])

chat_history = []

#reads chat history from chat history (txt file in this case) and stores in variable
with open('chat_history.txt') as f:
  chat_history.extend(f.readlines())

prompt = chat_template.invoke({
  'profession':'cricketer',
  'topic':'googly'},
  'chat_history':chat_history})

response = model.invoke(prompt)

print(response.content)
