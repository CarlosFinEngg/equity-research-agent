"""Equity researcher: provide reasonable stock analysis"""

import datetime
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
# from google.adk.tools import google_search

from stock_analysis_agent.sub_agents import fund_agent, policy_agent, technical_agent

from . import prompt
from .config import MODEL
from .sub_agents.fundamental_agent import fundamental_agent
from .sub_agents.technical_agent import technical_agent
from .sub_agents.fund_agent import fund_agent
from .sub_agents.policy_agent import policy_agent


def get_current_time() -> dict:
    """Returns the current date and time.

    Args:
        None

    Returns:
        dict: status and result.
    """

    now = datetime.datetime.now()
    report = (
        f'The current time is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


root_agent = LlmAgent(
    name="equity_researcher",
    model=MODEL,
    description=(
        "Agent to analyse a stock from fundamental, technical, fund flow, and political perspectives."
    ),
    instruction=prompt.EQUITY_RESEARCHER_PROMPT,
    tools=[get_current_time,
           AgentTool(agent=fundamental_agent),
           AgentTool(agent=technical_agent),
           AgentTool(agent=fund_agent),
           AgentTool(agent=policy_agent)],
    output_key="equity_researcher_output"
)

