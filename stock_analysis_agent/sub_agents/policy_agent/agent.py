from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, SseServerParams
from google.adk.tools import google_search

from . import prompt
from ...config import MODEL

policy_agent = LlmAgent(
    model=MODEL,
    name="policy_agent",
    description="policy_agent for conducting policy and regulatory analysis using government announcements, regulatory policies, industry guidelines, and legislative data.",
    instruction=prompt.POLICY_AGENT_PROMPT,
    output_key="policy_analysis_output",
    tools=[google_search]
)