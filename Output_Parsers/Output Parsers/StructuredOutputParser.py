#basically gives output in which ever format we specify

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

schema=[
ResponseSchema(name='Fact 1',description='Fact 1 about the topic'),
ResponseSchema(name='Fact 2',description='Fact 2 about the topic'),
ResponseSchema(name='Fact 3',description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

prompt = PromptTemplate(
template ='Give me 3 Facts about {topic}\n{format_instruction}',
input_variables=['topic'],
partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = prompt | model | parser
res = chain.invoke({'topic':'Sleeping'})
print(res)
