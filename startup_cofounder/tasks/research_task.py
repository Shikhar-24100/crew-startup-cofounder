from crewai import Task

def research_task(idea: str, agent):
    return Task(
        description=f"""
        Analyze this startup idea: "{idea}"
        
        Your research must cover:
        1. **Target Market** — Who exactly is the customer? Be specific (not "everyone").
        2. **Market Size** — TAM/SAM/SOM estimate with reasoning.
        3. **Top 3 Competitors** — Name them, their strengths, and their weaknesses.
        4. **Core Customer Pain** — What specific frustration does this solve?
        5. **Market Trends** — What tailwinds (or headwinds) exist right now?
        
        Be specific and concise. No fluff. Max 400 words.
        """,
        expected_output=(
            "A structured market analysis with sections for: Target Market, "
            "Market Size, Competitors, Customer Pain Points, and Market Trends. "
            "Bullet points preferred. Under 400 words."
        ),
        agent=agent,
    )