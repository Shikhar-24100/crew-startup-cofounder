from crewai import Crew, Process
from agents.market_researcher import market_researcher
from agents.tech_architect import tech_architect
from agents.devil_advocate import devil_advocate
from agents.pitch_writer import pitch_writer
from tasks.research_task import research_task
from tasks.architecture_task import architecture_task
from tasks.critique_task import critique_task
from tasks.pitch_task import pitch_task
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import json, os

console = Console()

def run_startup_crew(idea: str):
    console.print(Panel.fit(
        f"[bold cyan]🚀 Startup Co-Founder System[/bold cyan]\n[yellow]Idea:[/yellow] {idea}",
        border_style="cyan"
    ))

    # Wire tasks to agents
    rt = research_task(idea, market_researcher())
    at = architecture_task(idea, tech_architect(), [rt])
    ct = critique_task(idea, devil_advocate(), [rt, at])
    pt = pitch_task(idea, pitch_writer(), [rt, at, ct])

    crew = Crew(
        agents=[market_researcher(), tech_architect(), devil_advocate(), pitch_writer()],
        tasks=[rt, at, ct, pt],
        process=Process.sequential,
        verbose=True,
    )

    console.print("\n[bold green]🤖 Agents are thinking...[/bold green]\n")
    result = crew.kickoff()

    # Save output
    os.makedirs("output", exist_ok=True)
    with open("output/result.md", "w", encoding="utf-8") as f:
        f.write(f"# Startup Analysis: {idea}\n\n")
        f.write(str(result))

    console.print(Panel.fit(
        "[bold green]✅ Done! Check output/result.md[/bold green]",
        border_style="green"
    ))

    return result


if __name__ == "__main__":
    import sys
    idea = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("💡 Enter your startup idea: ")
    run_startup_crew(idea)