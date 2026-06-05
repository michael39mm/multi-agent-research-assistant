from dotenv import load_dotenv
from langchain_groq import ChatGroq
from models.research_plan import ResearchPlan

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


def planner_node(state):

    query = state["query"]

    prompt = f"""
    You are a senior research strategist.

    Your job is to create a comprehensive research plan.

    Break the following research topic into
    3 research questions.

    The questions should:
    - cover the topic comprehensively
    - avoid overlap
    - be specific enough to investigate

    Research Topic:
    {query}
    """

    structured_llm = llm.with_structured_output(ResearchPlan)

    response = structured_llm.invoke(prompt)

    return {
        "research_plan": response.research_questions
    }