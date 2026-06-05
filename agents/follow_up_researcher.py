from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools.search import search_web


load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def follow_up_researcher_node(state):
    additional_findings = []
    for item in state["knowledge_gaps"]:
        question = item["question"]
        finding = item["finding"]
        weaknesses = item["weaknesses"]
        assessment = item["assessment"]
        knowledge_gaps = item["knowledge_gaps"]

        sources = search_web(
    f"{question} {knowledge_gaps}"
)

        source_text = "\n\n".join(
    [
        f"Title: {source['title']}\n"
        f"Content: {source['content'][:500]}"
        for source in sources
    ]
)

        print(f"Conducting follow-up research for: {question}")
        prompt = f"""
You are a senior research analyst.

Your task is to investigate a specific knowledge gap identified during a research review.

Original Research Question:
{question}

Previous Critique Weaknesses:
{weaknesses}

Previous Assessment:
{assessment}

Original Finding:
{finding}

Identified Knowledge Gap:
{knowledge_gaps}

Evidence:
{source_text}

Your objective is to gather additional evidence that directly addresses the knowledge gap.

Requirements:
- Use ONLY the supplied evidence.
- Do not invent studies, statistics, surveys, costs, percentages, or sources.
- Focus only on the identified knowledge gap.
- Provide new information not already present in the original finding.
- Include quantitative evidence whenever possible.
- Discuss uncertainties and limitations.
- Be objective and evidence-based.
- Do not repeat the original finding.
- Limit the response to 2-4 paragraphs.

Return only the additional research finding.
"""

        response = llm.invoke(prompt)
        additional_findings.append(
    {
        "question": question,
        "finding": finding,
        "weaknesses": weaknesses,
        "assessment": assessment,
        "knowledge_gaps": knowledge_gaps,
        "additional_findings": response.content,
        "sources": [
            source["url"]
            for source in sources
        ]
    }
)
    return {
            "additional_findings": additional_findings,
            "iteration_count": state["iteration_count"] + 1
        }