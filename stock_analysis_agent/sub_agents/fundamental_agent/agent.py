from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

from . import prompt
from ...config import MODEL

fundamental_agent = LlmAgent(
    model=MODEL,
    name="fundamental_agent",
    description="fundamental_agent for conducting fundamental analysis using financial statements",
    instruction=prompt.FUNDAMENTAL_AGENT_PROMPT,
    output_key="fundamental_analysis_output",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                    command="uv",
                    args=[
                        "--directory",
                        "/home/tic19/PyProjects/equity-research-agent/yahoo-finance-mcp",
                        "run",
                        "server.py"
                    ]
            ),
            tool_filter=['get_financial_statement']
        ),
    ]
)