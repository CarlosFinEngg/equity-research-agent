from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


from . import prompt
from ...config import MODEL
from .tools import calculate_technical_indicators


technical_agent = LlmAgent(
    model=MODEL,
    name="technical_agent",
    description="technical_agent for conducting technical analysis using historical price data and indicators and output a structured Markdown report.",
    instruction=prompt.TECHNICAL_AGENT_PROMPT,
    output_key="technical_analysis_output",
    tools=[calculate_technical_indicators]
)