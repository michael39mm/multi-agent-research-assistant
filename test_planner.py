from agents.planner import planner_node


state = {
    "query": "Research whether electric vehicles are more environmentally friendly than gasoline vehicles."
}


result = planner_node(state)

print(result)