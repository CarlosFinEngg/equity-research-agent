from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm

from . import prompt
from .config import MODEL, GEMINI_LIST

from .sub_agents.fundamental_agent.agent import fundamental_agent
from .sub_agents.technical_agent.agent import technical_agent
from .sub_agents.fund_agent.agent import fund_agent
from .sub_agents.policy_agent.agent import policy_agent

from .tools import *


if MODEL in GEMINI_LIST:
    model_in_use = MODEL
else:
    model_in_use = LiteLlm(model=MODEL)


analysis_agent = SequentialAgent(
    name="equity_research_pipeline",
    description=(
        "Agent to analyse a stock from fundamental, technical, fund flow, and political perspectives and report findings into a structured detailed Markdown report in Chinese."
    ),
    sub_agents=[
        fundamental_agent,
        technical_agent,
        fund_agent,
        policy_agent
        ]
)


root_agent = LlmAgent(
    name="coordinator_agent",
    model=model_in_use,
    description=(
        "Agent to coordinate input taking, analyses conducting, and report consolidation."
    ),
    instruction="""
        Role: coordinate input taking, analyses conducting, and report consolidation
        tools: get_current_time, analysis_agent, combine_reports

        Primary Goal:
        Your primary goal is to coordinate the input taking, analyses conducting, and report consolidation process. Procedures are as follows:
        1. Collect provided_ticker from user input and store it in session.state and then use google_search_agent to find company nameand store it in session.state. If the user does not provide a ticker but instead a stock name, use google_search_agent to find the corresponding ticker (should be a 6-digit code) and store it in session.state.
        2. Pass provided_ticker to analysis_agent to conduct analyses on the provided_ticker.
        3. call combine_reports to consolidate the outputs from subagents into a structured detailed Markdown report in Chinese as convert it to pdf or html file as per user's choice.
    """,
    tools=[get_current_time,
           AgentTool(agent=google_search_agent),
           AgentTool(agent=analysis_agent),
           combine_reports],
    output_key="root_agent_output"
)








