from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import load_prompt
from dotenv import load_dotenv

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
prompt = load_prompt('template.json')

final = prompt.invoke(
    {
    'profession':'gamer', 
    'topic':'lurking'
    }
)

responce = model.invoke(final_prompt)
print(response.content)
