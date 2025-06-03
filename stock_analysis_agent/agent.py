"""Equity researcher: provide reasonable stock analysis"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm

# from stock_analysis_agent.sub_agents import fund_agent, policy_agent, technical_agent

from . import prompt
from .config import *
from .sub_agents.fundamental_agent import fundamental_agent
from .sub_agents.technical_agent import technical_agent
from .sub_agents.fund_agent import fund_agent
from .sub_agents.policy_agent import policy_agent
from .tools import *


if MODEL in GEMINI_LIST:
    model_in_use = MODEL
else:
    model_in_use = LiteLlm(model=MODEL)

root_agent = LlmAgent(
    name="equity_researcher",
    model=model_in_use,
    description=(
        "Agent to analyse a stock from fundamental, technical, fund flow, and political perspectives and consolidate findings into a structured detailed Markdown report in Chinese."
    ),
    instruction=prompt.EQUITY_RESEARCHER_PROMPT,
    tools=[get_current_time,
           AgentTool(agent=google_search_agent),
           AgentTool(agent=fundamental_agent),
           AgentTool(agent=technical_agent),
           AgentTool(agent=fund_agent),
           AgentTool(agent=policy_agent),
           combine_reports],
    output_key="root_agent_output"
)




