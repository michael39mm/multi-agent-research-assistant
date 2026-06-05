from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def gap_finder_node(state):
    knowledge_gaps = []
    for item in state["criticisms"]:
        question = item["question"]
        finding = item["finding"]
        score = item["score"]
        strengths = item["strengths"]
        weaknesses = item["weaknesses"]
        assessment = item["assessment"]

        print(f"Finding gaps for: {question}")
        prompt = f"""
You are a senior research director.

Your task is to identify missing knowledge gaps based on a research finding and its critique.

Research Question:
{question}

Research Finding:
{finding}

Critique Score:
{score}

Strengths:
{strengths}

Weaknesses:
{weaknesses}

Assessment:
{assessment}

Analyze the critique and determine:

1. What important information is still missing?
2. What evidence would strengthen the finding?
3. What follow-up investigation should be conducted?

Generate 1 to 3 specific follow-up research tasks.

Requirements:
- Tasks must be actionable.
- Tasks must be specific and researchable.
- Do not repeat the original research question.
- Focus on addressing weaknesses identified in the critique.
- Prioritize evidence gathering and missing information.

Return only the follow-up research tasks as a numbered list.
"""

        response = llm.invoke(prompt)
        knowledge_gaps.append(
    {
        "question": question,
        "finding": finding,
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "assessment": assessment,
        "knowledge_gaps": response.content
    }
)
    return {"knowledge_gaps": knowledge_gaps}
