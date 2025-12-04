from langchain.agents import create_agent
from .system_prompt import system_prompt
from src.tools import pdf_tools
from src.model import model


def planner_agent():
    agent = create_agent(
        model=model,
        tools=pdf_tools,
        system_prompt=system_prompt,
    )   
    return agent