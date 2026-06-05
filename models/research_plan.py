from pydantic import BaseModel
from typing import List


class ResearchPlan(BaseModel):
    research_questions: List[str]