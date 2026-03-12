from crewai import Task

def architecture_task(idea: str, agent, context_tasks: list):
    return Task(
        description=f"""
        Based on the market research provided, design the technical plan for: "{idea}"
        
        Cover:
        1. **Recommended Tech Stack** — Frontend, backend, database, infra. Justify each choice.
        2. **MVP Scope** — What are the 3-5 core features for v1? What do you cut?
        3. **Build Time Estimate** — Solo founder vs small team (2-3 devs).
        4. **Technical Moat** — Is there anything technically defensible here?
        5. **Top 3 Technical Risks** — What could break this technically?
        
        Think pragmatically. Ship fast. No over-engineering. Max 400 words.
        """,
        expected_output=(
            "A technical architecture plan with: Tech Stack, MVP Feature List, "
            "Build Timeline, Technical Moat analysis, and Risk flags. Under 400 words."
        ),
        agent=agent,
        context=context_tasks,
    )