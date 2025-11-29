from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from dotenv import load_dotenv
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent,AgentExecutor
from langchain_classic import hub

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

search_tool = DuckDuckGoSearchRun()

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=model,
    tools=[search_tool],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

response = agent_executor.invoke({"input": "Find the capital of Telangana, then find it's cheif minister"})
print(response)




