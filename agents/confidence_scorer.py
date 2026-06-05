from tools.research_memory import save_to_memory

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from models.critique import Critique

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


def confidence_scorer_node(state):

    evaluation = state["evaluation"]

    audit_results = state["audit_results"]

    prompt = f"""
You are a research confidence evaluator.

Research Evaluation:
{evaluation}

Source Audit:
{audit_results}

Determine an overall confidence score from 0 to 100.

Consider:

- Research quality score
- Evidence support strength
- Identified weaknesses
- Remaining uncertainties

Return:

Confidence Score:
<number>

Explanation:
<short paragraph>
"""

    response = llm.invoke(prompt)
    save_to_memory(
        {
            "query": state["query"],
            "report": state["final_report"],
            "confidence_score": response.content
        }
    )
    return {
        "confidence_score": response.content
    }