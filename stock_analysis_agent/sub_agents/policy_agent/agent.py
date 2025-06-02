from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.tools import google_search
from dotenv import load_dotenv
import os

from . import prompt
from ...config import MODEL


# Load environment variables from .env file
load_dotenv(dotenv_path="stock_analysis_agent/.env")

# Get the API key
smithery_api_key = os.getenv("SMITHERY_API_KEY")


policy_agent = LlmAgent(
    model=MODEL,
    name="policy_agent",
    description="policy_agent for conducting policy and regulatory analysis using government announcements, regulatory policies, industry guidelines, and legislative data and output a structured Markdown report.",
    instruction=prompt.POLICY_AGENT_PROMPT,
    output_key="policy_analysis_output",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    "-y",
                    "@smithery/cli@latest",
                    "run",
                    "@smithery-ai/server-sequential-thinking",
                    "--key",
                    f"{smithery_api_key}"
                ]
            )
        ),
        google_search
    ]
)
