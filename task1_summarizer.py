
!pip install transformers torch

from transformers import pipeline

summarizer = pipeline("summarization")

text = """
Artificial Intelligence (AI) is a branch of computer science that aims to create machines 
that can perform tasks which normally require human intelligence. These tasks include things 
like visual perception, speech recognition, decision-making, and language translation. 
AI has the potential to transform many industries by automating processes, improving efficiency, 
and enabling new products and services.
"""


summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

print("=== Input Text ===")
print(text)
print("\n=== Generated Summary ===")
print(summary[0]['summary_text'])

