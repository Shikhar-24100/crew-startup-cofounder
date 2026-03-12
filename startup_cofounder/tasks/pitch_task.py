from crewai import Task

def pitch_task(idea: str, agent, context_tasks: list):
    return Task(
        description=f"""
        You have all the research, architecture, and critique for: "{idea}"
        
        Now write the full investor pitch document. Structure it as:
        
        ## 🚀 [Startup Name] — One-liner
        
        ### The Problem
        ### The Solution  
        ### Market Opportunity
        ### How It Works (Tech)
        ### Why Now
        ### Risks & How We Handle Them
        ### MVP Roadmap (3 months)
        ### The Ask / Call to Action
        
        Make it punchy. Use storytelling. Open with a hook. 
        This should make someone lean forward. Max 600 words.
        """,
        expected_output=(
            "A complete, compelling startup pitch document following the 8-section structure. "
            "Written in a narrative, investor-ready style. Under 600 words."
        ),
        agent=agent,
        context=context_tasks,
    )