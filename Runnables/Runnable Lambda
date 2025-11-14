from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def word_count(text):
    return len(text.split())

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
    'count':RunnableLambda(word_count)
})

final_chain = joke_generator | parallel_process
result = final_chain.invoke({'topic':'football'})

print('The joke:')
print(result['print'])

print('No of words:')
print(result['count'])
