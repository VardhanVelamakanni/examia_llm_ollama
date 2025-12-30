from content_builder import build_content
from llm_client import ask_llm

print("Building content...")
content = build_content(
    pdf_path="sample.pdf",
    ppt_path="sample.pptx"
)

content = content[:1500]

# ------------------ QUESTIONS ------------------

questions_prompt = f"""
From the text below, generate ONLY 3 exam-oriented questions.
Do not include answers.

Text:
{content}
"""

questions = ask_llm(questions_prompt)

print("\nQUESTIONS:\n")
print(questions)

# ------------------ ANSWERS ------------------

answers_prompt = f"""
Answer the following questions clearly and concisely.
Limit each answer to 3–4 lines.

Questions:
{questions}
"""

answers = ask_llm(answers_prompt)

print("\nANSWERS:\n")
print(answers)

# ------------------ TOPIC BASIC INFORMATION ------------------

topics_prompt = f"""
From the text below, identify the main topics.
For each topic, give basic information suitable for quick exam revision.

Rules:
- Short explanations (3–4 lines per topic)
- Simple language
- No extra topics outside the text

Text:
{content}
"""

topics_info = ask_llm(topics_prompt)

print("\nTOPIC BASIC INFORMATION:\n")
print(topics_info)