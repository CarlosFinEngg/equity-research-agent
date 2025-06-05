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
- Flexible report output formats (PDF/HTML) with full Chinese language support

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
- Developed and tested on Linux. Performance on Windows is not garanteed.
- Python 3.11+
- Dependencies as listed in pyproject.toml, including:
  - [google-adk](https://pypi.org/project/google-adk/)
  - [mcp-query-table](https://pypi.org/project/mcp-query-table/)
  - [mcp](https://pypi.org/project/mcp/)
  - [pypandoc](https://pypi.org/project/pypandoc/) for PDF/HTML report generation

For PDF report generation with Chinese support, additional dependencies are required:

1. Install Pandoc using Python:
```python
import pypandoc
# Install pandoc
pypandoc.download_pandoc()
```

2. Install XeTeX and Noto CJK fonts on Linux:
```bash
sudo apt update
sudo apt install texlive-xetex fonts-noto-cjk
```

Please note: For the setup of MCP servers, please refer to the following:
  - [sequential-thinking](https://smithery.ai/server/@smithery-ai/server-sequential-thinking)

MCPs are supposed to be cloned to this project's root folder.

Install dependencies:
```bash
uv pip install .
```


## Usage

Configure models and environment variables in `stock_analysis_agent/config.py` and `.env` as needed.

Then run the agent in ADK WEB:
```bash
adk web
```

The analysis report will be generated in both Markdown format and your chosen output format (PDF/HTML). The reports can be found in the `reports` directory with the following naming convention:
```
reports/
    equity_research_report_<company_name>_<ticker>_<YYYYMMDD>.md
    equity_research_report_<company_name>_<ticker>_<YYYYMMDD>.pdf  # or .html
```


## License
MIT

## Disclaimer
This project is for informational purposes and does not constitute financial advice.
