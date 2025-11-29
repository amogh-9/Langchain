from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel,Field

class MultiInput(BaseModel):
    a : int = Field(description='First number to multiply',required='True')
    b : int = Field(description='Second number to multiply',required='True')

class MultiplyTool(BaseTool):
    name : str = "Multiply"
    description : str = "Multiply two numbers"
    args_schema:Type[BaseModel] = MultiInput

    def _run(self, a:int ,b:int ) -> int:
        return a*b

multiply_tool = MultiplyTool()
result = multiply_tool.invoke({'a':10,'b':2})
print(result)
