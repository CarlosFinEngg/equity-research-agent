import os
import pypandoc
from datetime import datetime
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import google_search

from .config import *





def get_current_time() -> dict:
    """Returns the current date and time.

    Args:
        None

    Returns:
        dict: current date and time.
    """

    now = datetime.now()
    report = f'The current time is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"current date and time": report}



google_search_agent = LlmAgent(
    model=GEMINI_LIST[0],
    name='google_search_agent',
    instruction="""
    You're a spealist in Google Search who take a search query and return the results.
    """,
    tools=[google_search]
)



def combine_reports(provided_ticker: str, company_name: str, output_format: str = 'pdf') -> dict:
    """
    Combines Markdown files from a hard-coded 'reports' folder into a single report.
    
    Args:
        provided_ticker (str): Stock ticker symbol, must be a string.
        company_name (str): Name of the company, must be a string.
        output_format (str, optional): Output format, either 'pdf' or 'html'. Defaults to 'pdf'.
    
    Returns:
        dict: A dictionary containing status information with the following structure:
            On success: {"status": "success", "output_report_name": str, "output_format": str}
            On error: {"status": "error", "error_message": str}
    """
    # Hard-coded input folder
    input_folder = 'reports'
    # Generate date string in YYYYMMDD format
    date_str = datetime.now().strftime('%Y%m%d')
    # Validate inputs
    if not isinstance(provided_ticker, str):
        return {"status": "error", "error_message": "provided_ticker must be a string"}
    if not isinstance(company_name, str):
        return {"status": "error", "error_message": "company_name must be a string"}
    
    # Construct output basename with underscores
    output_basename = f"equity_research_report_{company_name}_{provided_ticker}_{date_str}"
    combined_md_path = os.path.join(input_folder, f"{output_basename}.md")

    try:
        # Define the expected order of files
        categories = ['fundamental', 'technical', 'fund', 'policy']
        
        # Ensure reports directory exists
        os.makedirs(input_folder, exist_ok=True)
        
        # Create YAML front matter
        yaml_front_matter = f"""
            ---
            title: "{company_name}（{provided_ticker}）基本面分析报告"
            author: "Equity Research Agent Created by Carlos Yaran Zhou"
            date: "{datetime.now().strftime('%Y-%m-%d')}"
            fontsize: 12pt
            lang: zh-CN
            mainfont: Noto Serif CJK SC
            monofont: Noto Sans Mono CJK SC
            output:
            pdf_document:
                latex_engine: xelatex
            ---

            """
        # Combine Markdown files
        with open(combined_md_path, 'w', encoding='utf-8') as outfile:
            # Write YAML front matter first
            outfile.write(yaml_front_matter)
            
            # Write content from each category
            for category in categories:
                filename = f"{category}_agent_report.md"
                filepath = os.path.join(input_folder, filename)
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(f"<!-- ===== {category.upper()} SECTION ===== -->\n\n")
                        outfile.write(content + "\n\n")
                else:
                    print(f"Warning: {filename} not found in {input_folder}. Skipping...")

        # Normalize output_format
        output_format = output_format.lower()
        if output_format not in ['pdf', 'html']:
            output_format = 'pdf'  # Default to PDF if invalid format specified

        output_file = os.path.join(input_folder, f"{output_basename}.{output_format}")
        # Convert to desired format
        if output_format == 'pdf':
            pypandoc.convert_file(combined_md_path, 'pdf', outputfile=output_file, extra_args=["--pdf-engine=xelatex"])
        else:
            pypandoc.convert_file(combined_md_path, 'html', outputfile=output_file)

        return {
            "status": "success",
            "output_report_name": output_basename,
            "output_format": output_format.upper()
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error occurred during output: {str(e)}"
        }





