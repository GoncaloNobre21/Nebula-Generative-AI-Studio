from langchain.prompts import PromptTemplate

# Prompt Template for Text Summarization
SUMMARIZATION_PROMPT = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in a concise and professional manner:\n\n{text}\n\nSummary:"
)

# Prompt Template for Creative Writing
CREATIVE_WRITING_PROMPT = PromptTemplate(
    input_variables=["topic"],
    template="Write a creative and engaging story about {topic}. Ensure the narrative is compelling and well-structured."
)

# Prompt Template for Detailed Code Explanation
CODE_EXPLANATION_PROMPT = PromptTemplate(
    input_variables=["code"],
    template="Explain the following code snippet in detail, focusing on its functionality and complexity:\n\n```python\n{code}\n```\n\nExplanation:"
)
