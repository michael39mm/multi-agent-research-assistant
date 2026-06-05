from dotenv import load_dotenv
from langchain_groq import ChatGroq

from models.critique import Critique

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

structured_llm = llm.with_structured_output(Critique)


def critic_node(state):

    criticisms = []

    for item in state["findings"]:

        question = item["question"]
        finding = item["finding"]

        print(f"Critiquing finding: {question}")

        prompt = f"""
You are a senior research reviewer.

Your task is to critically evaluate the following research finding.

Research Question:
{question}

Research Finding:
{finding}

Evaluate the finding on:

1. Completeness
2. Evidence Strength
3. Balance
4. Limitations

Additionally assign a quality score from 1-10.

Scoring Guide:

1-3:
Poor quality, unsupported claims, major gaps.

4-6:
Partially supported but significant weaknesses.

7-8:
Strong finding with minor weaknesses.

9-10:
Excellent, comprehensive, and well-supported.

Return:

- score
- strengths
- weaknesses
- assessment
"""

        critique = structured_llm.invoke(prompt)

        criticisms.append(
            {
                "question": question,
                "finding": finding,
                "score": critique.score,
                "strengths": critique.strengths,
                "weaknesses": critique.weaknesses,
                "assessment": critique.assessment
            }
        )
    scores = [item["score"] for item in criticisms]
    average_score = sum(scores) / len(scores)
    return {
        "criticisms": criticisms,
        "evaluation": {
        "average_score": average_score
    }
    }