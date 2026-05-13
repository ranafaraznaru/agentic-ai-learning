from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
import json


os.environ['LANGCHAIN_PROJECT'] = 'ReAct Agent'
load_dotenv()
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key={WEATHERSTACK_API_KEY}&query={city}'

  response = requests.get(url)

  return json.dumps(response.json())

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)


# Step 3: Create the agent using create_agent
agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful assistant."
)



# Step 4: Invoke
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is the current temp of faisalabad"
        }
    ]
})
print(response["messages"][-1].content)
