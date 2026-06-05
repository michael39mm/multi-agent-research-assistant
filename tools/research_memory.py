import json
import os

MEMORY_FILE = "memory/research_memory.json"


def save_to_memory(report):

    os.makedirs("memory", exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        memory = []
    else:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)

    memory.append(report)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)