from google.adk.agents import Agent

from agents.skills_agent import skills_agent
from agents.summary_agent import summary_agent
from agents.projects_agent import projects_agent
from agents.experiences_agent import experiences_agent
from agents.educations_agent import educations_agent


resume_agent = Agent(
    name="resume_agent",
    model="gemini-2.0-flash",

    instruction="""
You are Resume Agent.

Responsibilities:
- Manage all resume editing requests
- Identify which resume section should be modified
- Route requests to the correct sub-agent

Routing:
- Skills → skills_agent
- Summary → summary_agent
- Projects → projects_agent
- Experiences → experiences_agent
- Education → educations_agent

Rules:
- Never directly modify resume data
- Delegate work to sub-agents
- Preserve JSON structure
- Ask clarification if request is unclear
""",

    sub_agents=[
        skills_agent,
        summary_agent,
        projects_agent,
        experiences_agent,
        educations_agent
    ]
)

print("Resume Agent Loaded")