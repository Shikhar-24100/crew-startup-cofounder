from crewai import Agent
from crewai_tools import SerperDevTool
from llm_config import get_llm

def devil_advocate():
    return Agent(
        role="Devil's Advocate",
        goal=(
            "Search the web for startups that already tried this idea and FAILED. "
            "Find real failure post-mortems, real reasons companies in this space shut down, "
            "and real obstacles. Then stress-test the current idea against those findings."
        ),
        backstory=(
            "You are a veteran startup critic who researches failure. You search for "
            "real companies that tried similar ideas, read their post-mortems, and use "
            "that to brutally stress-test new ideas. You never criticize without evidence."
        ),
        tools=[SerperDevTool()],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
    )