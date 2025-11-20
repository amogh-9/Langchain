from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda,RunnablePassthrough,RunnableBranch
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a repot on {topic}',
    input_variables=['topic'],
    validate_template=True
)

prompt2 = PromptTemplate(
    template='Generate a summary of the text {text}',
    input_variables=['text'],
    validate_template=True
)

repot_generator = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>100,RunnableLambda(lambda x:print('Report') or x) | prompt2 | model | parser),
    RunnableLambda(lambda x:print('Summary') or x) | RunnablePassthrough()
)

final_chain = repot_generator | branch_chain
result = final_chain.invoke({'topic':'football'})

print(result)
