from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_web(query):

    results = client.search(
        query=query,
        max_results=2
    )

    return results["results"]

    