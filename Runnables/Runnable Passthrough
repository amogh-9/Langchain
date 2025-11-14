from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a joke on {topic}',
    input_variables=['topic'],
    validate_template=True
)

prompt2 = PromptTemplate(
    template='Explain the joke : {joke}',
    input_variables=['joke'],
    validate_template=True
)

joke_generator = prompt1 | model | parser

parallel_process = RunnableParallel({
    'print':RunnablePassthrough(),
    'explain': prompt2 | model | parser
})

final_chain = joke_generator | parallel_process
result = final_chain.invoke({'topic':'football'})

print('The joke:')
print(result['print'])

print('Explaination:')
print(result['explain'])
