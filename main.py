from workflows.graph import build_graph
import traceback
graph = build_graph()

try:

    result = graph.invoke(
        {
            "query": "What are the most effective strategies for retrofitting educational buildings to improve energy efficiency and indoor environmental quality?",
            "iteration_count": 0
        }
    )

    print(result)
    print(result["confidence_score"])
    print(result["final_report"][:1000])

except Exception as e:
    traceback.print_exc()