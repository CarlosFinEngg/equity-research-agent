from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

from . import prompt
from ...config import MODEL
from .tools import fetch_stock_financial_indicators, get_current_time


fundamental_agent = LlmAgent(
    model=MODEL,
    name="fundamental_agent",
    description="fundamental_agent for conducting fundamental analysis using financial statements and output a structured Markdown report.",
    instruction=prompt.FUNDAMENTAL_AGENT_PROMPT,
    output_key="fundamental_analysis_output",
    tools=[
        fetch_stock_financial_indicators,
        get_current_time
    ]
)