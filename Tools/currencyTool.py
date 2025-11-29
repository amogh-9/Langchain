import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.messages import HumanMessage,SystemMessage

load_dotenv()

@tool
def get_conversion_rate(base_currency: str, target_currency: str) -> float:
    """
    Convert currency from base_currency to target_currency.

    The LLM can extract ISO codes from natural language:
    - dollars → USD
    - rupees → INR
    - euros → EUR
    - yen → JPY
    - etc.

    It MUST pass ISO codes like: {"base_currency":"USD","target_currency":"INR"}.
    """
    url = f'https://v6.exchangerate-api.com/v6/API_KEY/latest/{base_currency}'
    data = requests.get(url).json()
    return data["conversion_rates"][target_currency]


model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
).bind_tools([get_conversion_rate])


user_query = HumanMessage("What is the conversion rate for dollars to rupees?")
messages =[user_query]
ai_message = model.invoke(messages)
#print(ai_message.tool_calls)
messages.append(ai_message)


tool = get_conversion_rate.invoke(ai_message.tool_calls[0])
messages.append(tool)

#print(messages)

result = model.invoke(messages)
print(result.content)


