from typing import TypedDict, List, Dict


class ResearchState(TypedDict):
    query: str

    research_plan: List[str]

    findings: List[dict]

    analysis: str

    criticisms: List[dict]

    knowledge_gaps: List[dict]

    additional_findings: List[dict]

    final_report: str

    audit_results: str
    
    evaluation: Dict

    confidence_score: str
    
    iteration_count: int

    

