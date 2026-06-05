from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools.search import search_web

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


def researcher_node(state):

    findings = []

    for question in state["research_plan"]:

        print(f"Researching: {question}")

        # Search the web
        sources = search_web(question)

        # Convert search results into text
        source_text = "\n\n".join(
    [
        f"Title: {source['title']}\n"
        f"Content: {source['content'][:500]}"
        for source in sources
    ]
)

        prompt = f"""
You are an expert research analyst.

Research Question:
{question}

Evidence:
{source_text}

Your task is to answer the research question using ONLY the evidence provided.

Requirements:
- Use only the supplied evidence.
- Do not invent studies, statistics, or sources.
- Be objective and balanced.
- Mention important limitations or tradeoffs.
- If evidence is conflicting, acknowledge it.
- Limit the response to 2-4 paragraphs.

Return only the research finding.
"""

        response = llm.invoke(prompt)

        findings.append(
            {
                "question": question,
                "finding": response.content,
                "sources": [
                    source["url"]
                    for source in sources
                ]
            }
        )

    return {
        "findings": findings
    }