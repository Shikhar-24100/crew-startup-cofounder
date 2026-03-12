from crewai import Task

def critique_task(idea: str, agent, context_tasks: list):
    return Task(
        description=f"""
        You've reviewed the market research and technical architecture for: "{idea}"
        
        Now ruthlessly stress-test it:
        1. **The Fatal Flaw** — What single thing could kill this company dead?
        2. **Weak Assumptions** — List 3 things the team is assuming that might be wrong.
        3. **Why Customers Won't Switch** — What's the real switching cost/inertia problem?
        4. **The "Why Now?" Challenge** — Has this been tried before? Why did it fail?
        5. **Suggested Mitigations** — For each flaw, suggest one concrete fix.
        
        Be harsh but fair. End on what would make you believe in this. Max 400 words.
        """,
        expected_output=(
            "A critical analysis with: Fatal Flaw, Weak Assumptions, Switching Cost problem, "
            "Why Now challenge, and Suggested Mitigations. Under 400 words."
        ),
        agent=agent,
        context=context_tasks,
    )