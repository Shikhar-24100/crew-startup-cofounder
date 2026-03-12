from crewai import Agent
from crewai_tools import SerperDevTool
from llm_config import get_llm

def market_researcher():
    return Agent(
        role="Market Research Analyst",
        goal=(
            "Analyze the startup idea by SEARCHING the web for real data: "
            "actual competitor companies, real funding rounds, real market size reports, "
            "and current trends. Never make up numbers — find them."
        ),
        backstory=(
            "You are a sharp market research analyst with 10 years of experience "
            "at top VC firms. You always back your claims with real data from the web. "
            "You search for actual competitors, their funding, and real market reports."
        ),
        tools=[SerperDevTool()],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
    )