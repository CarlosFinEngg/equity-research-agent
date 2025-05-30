# Equity Research LLM Agent

A multi-agent Python system for comprehensive stock analysis and equity research reporting.

## Overview

**equity-research-agent** leverages multiple specialized sub-agents to perform:
- Fundamental analysis (financial statements, ratios, trends)
- Technical analysis (price data, indicators, chart patterns)
- Fund flow analysis (capital inflow/outflow, liquidity)
- Policy analysis (government/regulatory news)

The main agent coordinates these sub-agents and synthesizes their findings into a unified research report.

## Features
- Modular agent-based architecture
- Integrates Google Search and MCP tools for data gathering
- Generates detailed, structured equity research reports

## Project Structure

```
pyproject.toml
stock_analysis_agent/
    agent.py
    config.py
    ...
    sub_agents/
        fundamental_agent/
        fund_agent/
        policy_agent/
        technical_agent/
```

## Requirements
- Python 3.11+
- Dependencies as listed in pyproject.toml, including:
  - [google-adk](https://pypi.org/project/google-adk/)
  - [mcp-query-table](https://pypi.org/project/mcp-query-table/)
  - [mcp](https://pypi.org/project/mcp/)

Please note: For the setup of MCP servers, please refer to the following:
- [yahoo-finance-mcp](https://github.com/hwangwoohyun-nav/yahoo-finance-mcp)

MCPs are supposed to be cloned to this project's root folder.

Install dependencies:
```bash
uv pip install .
```


## Usage

Run the agent in ADK WEB:
```bash
adk web
```

Configure models and environment variables in `stock_analysis_agent/config.py` and `.env` as needed.

## License
MIT

## Disclaimer
This project is for informational purposes and does not constitute financial advice.
