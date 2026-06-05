from pydantic import BaseModel
from typing import List


class Critique(BaseModel):
    score: int
    strengths: List[str]
    weaknesses: List[str]
    assessment: str