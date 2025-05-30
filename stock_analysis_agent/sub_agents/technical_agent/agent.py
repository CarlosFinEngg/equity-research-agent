from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, SseServerParams
from google.adk.tools import google_search

from . import prompt
from ...config import MODEL

technical_agent = LlmAgent(
    model=MODEL,
    name="technical_agent",
    description="technical_agent for conducting technical analysis using historical price data and indicators",
    instruction=prompt.TECHNICAL_AGENT_PROMPT,
    output_key="technical_analysis_output",
    tools=[google_search]
)