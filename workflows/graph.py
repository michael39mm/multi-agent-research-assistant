from langgraph.graph import StateGraph, END
from agents.researcher import researcher_node
from models.state import ResearchState
from agents.planner import planner_node
from agents.critic import critic_node
from agents.gap_finder import gap_finder_node
from agents.follow_up_researcher import follow_up_researcher_node
from agents.report_writer import report_writer_node
from agents.source_auditor import source_auditor_node
from agents.confidence_scorer import confidence_scorer_node


def should_continue(state):

    scores = [
        item["score"]
        for item in state["criticisms"]
    ]

    average_score = sum(scores) / len(scores)

    if average_score >= 8:
        return "report_writer"

    if state["iteration_count"] >= 1:
        return "report_writer"

    return "gap_finder"


def build_graph():
    graph = StateGraph(ResearchState)
    graph.add_node("planner", planner_node)
    graph.set_entry_point("planner")
    graph.add_node("researcher", researcher_node)
    graph.add_node("critic",critic_node)
    graph.add_node("gap_finder",gap_finder_node)
    graph.add_node("follow_up", follow_up_researcher_node)
    graph.add_node("report_writer", report_writer_node)
    graph.add_node("source_auditor", source_auditor_node)
    graph.add_node("confidence_scorer", confidence_scorer_node)
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "critic")
    graph.add_conditional_edges("critic", should_continue,{ "report_writer": "report_writer", "gap_finder": "gap_finder" })
    graph.add_edge("gap_finder", "follow_up")
    graph.add_edge("follow_up", "report_writer")
    graph.add_edge("report_writer", "source_auditor")
    graph.add_edge("source_auditor", "confidence_scorer")
    graph.add_edge("confidence_scorer", END)
    return graph.compile()


