from langchain_community.tools import StructuredTool
from pydantic import BaseModel,Field

class MultiplyInput(BaseModel):
    a:int = Field(description="This is the first number to multiply",required=True)
    b:int = Field(description="This is the second number to multiply",required=True)

def multiply(a:int, b:int)->int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiplication",
    description="multiply two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({'a':3,'b':5})
print(result)