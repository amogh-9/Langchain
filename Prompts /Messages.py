from langchain_google_genai import ChatGoogelGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

message = [
  SystemMessage(content='You are a helpful assistant'),
  HumanMessage(content='Tell me in 2 lines about')
  }

result = model.invoke(message)
message.append(AIMessage(content=result.content)

print(message)
