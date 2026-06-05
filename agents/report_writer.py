from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


def report_writer_node(state):

    research_plan = state["research_plan"]

    findings = state["findings"]

    criticisms = state["criticisms"]

    additional_findings = state["additional_findings"]

    print("Writing final report...")

    prompt = f"""
You are a senior research report writer.

You have been provided with:

1. Research Questions
2. Original Findings
3. Critiques
4. Additional Findings

Research Questions:
{research_plan}

Original Findings:
{findings}

Critiques:
{criticisms}

Additional Findings:
{additional_findings}

Your task is to produce a professional research report.

Requirements:

* Integrate all findings into one coherent report.
* Use both original and follow-up research.
* Address limitations and uncertainties.
* Present balanced conclusions.
* Avoid repetition.
* Use professional academic language.
* Base all conclusions and recommendations on the available evidence.
* Do not make unsupported claims.
* Clearly acknowledge remaining uncertainties where evidence is limited.

Structure:

1. Executive Summary

2. Key Findings

3. Limitations and Critical Considerations

4. Final Conclusion

5. Overall Assessment and Recommendation

For Section 5, provide:

Overall Assessment:

* A concise synthesis of the overall evidence.
* Explain what the evidence collectively suggests.

Recommendation:

* Based on the available evidence, identify the most reasonable conclusion, strategy, or course of action.
* Recommendations must be evidence-based.
* Recommendations must acknowledge important limitations and uncertainties.
* Do not overstate confidence.
* If evidence is mixed or inconclusive, clearly state this.

Return only the report.

"""

    response = llm.invoke(prompt)

    return {
        "final_report": response.content
    }