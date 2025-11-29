from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

@tool
def add(a:int,b:int)->int:
    """Addtion of two numbers"""
    return a+b

@tool
def multiply(a:int,b:int)->int:
    """Multiplication of two numbers"""
    return a*b

llm_with_tools = model.bind_tools([add,multiply])

llm = llm_with_tools.invoke('What is sum of 2 and 3')
print(llm)


#manually running add fucntion from input give by llm
result = add.invoke(llm.tool_calls[0])
print(result)