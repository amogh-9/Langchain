from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = JsonOutputParser()

prompt = PromptTemplate(
    template='Give an imaginary person with name , age, gender and religion \n {format}',
    input_variables=[],
    partial_variables={'format':parser.get_format_instructions()}
)

chain = prompt | model | parser
result = chain.invoke({})

print(result)
