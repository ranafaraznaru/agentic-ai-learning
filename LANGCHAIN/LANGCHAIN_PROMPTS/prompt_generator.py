# we separated this template for re-use and generating the template.json

#prompt template in langchain is a structured way to create prompts dynamically by inserting variables into a predefined template.
#instead of hardcoding prompts PromptTemplate allows you to define placeholders that can be filled in at runtime with different inputs.
# Benifits , default validation, reusable like we did at bottom by saving it into a .json and its tightly coupled to lanchain ecosystem

from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where
applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient 
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables= ['paper_input', 'style_input', 'length_input']
)


template.save('template.json')