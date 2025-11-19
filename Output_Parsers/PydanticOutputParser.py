from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal,List


load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',temperature=0.9)

class Car(BaseModel):
    brand : str = Field(description='Name of the brand and name of car')
    cost : int = Field(description='Price of the car in rupees')
    version: Literal['Petrol', 'Diesel'] = Field(description='Only Petrol or Diesel allowed')

parser = PydanticOutputParser(pydantic_object=Car)

prompt = PromptTemplate(template = """
Give me a UNIQUE and DIFFERENT car every time.
It must:
- be legally available in India
- cost less than 10 lakh
- not repeat previous outputs
- choose from a wide variety of brands
- pick random variants
- pick random model years or editions

{format}""",
    input_variables={},
    partial_variables={'format':parser.get_format_instructions()}
)

chain = prompt | model | parser
result = chain.invoke({})
output = result.model_dump()
print(output)
