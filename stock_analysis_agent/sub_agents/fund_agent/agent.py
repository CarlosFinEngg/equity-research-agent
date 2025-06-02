from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


from . import prompt
from ...config import MODEL
from .tools import fetch_stock_individual_fund_flow, fetch_stock_chip_distribution, fetch_stock_institute_hold_detail, fetch_stock_hsgt_individual_detail, get_last_quarter




fund_agent = LlmAgent(
    model=MODEL,
    name="fund_agent",
    description="fund_agent for conducting fund flow analysis using fund flow data and output a structured Markdown report.",
    instruction=prompt.FUND_AGENT_PROMPT,
    output_key="fund_analysis_output",
    tools=[
        get_last_quarter,
        fetch_stock_individual_fund_flow,
        fetch_stock_chip_distribution,
        fetch_stock_institute_hold_detail,
        fetch_stock_hsgt_individual_detail
    ]
)