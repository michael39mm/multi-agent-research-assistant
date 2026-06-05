from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


def source_auditor_node(state):

    findings = state["findings"]
    additional_findings = state["additional_findings"]
    final_report = state["final_report"]

    prompt = f"""
You are a source verification specialist.

Original Findings:
{findings}

Additional Findings:
{additional_findings}

Final Report:
{final_report}

Your task is to evaluate whether the report is adequately supported by the available evidence.

Determine:

1. Are the major claims supported?
2. Are there unsupported statements?
3. Are there exaggerations?
4. Are important citations missing?

Provide:

Support Level:
- Strong
- Moderate
- Weak

Issues:
- bullet points

Summary:
- short paragraph
"""

    response = llm.invoke(prompt)

    return {
        "audit_results": response.content
    }