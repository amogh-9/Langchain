from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

template = PromptTemplate(
    template='You are an experienced {profession}, give me simple 2 line description of {topic}',
    input_variables=['profession','topic'],
    validate_template=True,
)

prompt = template.invoke({'profession':'Teacher','topic':'gravity'})
result = model.invoke(prompt)

print(result.content)
