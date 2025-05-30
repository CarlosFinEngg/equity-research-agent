from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, SseServerParams
from google.adk.tools import google_search

from . import prompt
from ...config import MODEL

fund_agent = LlmAgent(
    model=MODEL,
    name="fund_agent",
    description="fund_agent for conducting fund flow analysis using fund flow data",
    instruction=prompt.FUND_AGENT_PROMPT,
    output_key="fund_analysis_output",
    tools=[google_search]
)