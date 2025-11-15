from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Weather(BaseModel):
  type : str = Field(description = 'Choose it between freezing, warm and hot')
  advice: str = Field(description = 'Give advice based on weather type')

structured_model = model.with_structured_output(Weather)
result = structured_model.invoke('The temperature is 17 degrees celcius')
result_dict = result.model_dump()

print(result_dict)
