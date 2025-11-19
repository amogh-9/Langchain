from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a joke on {topic}',
    input_variables={'topic'}
)

prompt2 = PromptTemplate(
    template='Explain the joke \n {joke}',
    input_variables={'joke'}
)

result = RunnableSequence(prompt1,model,prompt2,model,parser)
print(result.invoke({'topic':'cricket'}))

