import streamlit as st
import openai

st.title("CV Analyzer — Sales Executive")

api_key = st.text_input("Enter OpenAI API Key", type="password")
cv = st.text_area("Paste CV text")
job = st.text_area("Paste Job Description")

if st.button("Analyze Candidate"):

    prompt = f"""
You are an AI recruitment evaluator.

Evaluate candidate against Sales Executive requirements.

SCORING CRITERIA (1 point each):
- Sales experience ≥2 years
- IT industry experience
- English proficiency
- Relevant sales skills
- Native Korean

HARD RULE:
If Korean is not native → Reject.

BONUS:
Chinese language

Return format:

Score: X/5

Matched:
✔
Missing:
✘

Bonus:
⭐ or none

Verdict:
5 Strong
3-4 Consider
0-2 Reject

Summary:
2 sentences.

JOB:
{job}

CV:
{cv}
"""

    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    st.subheader("Result")
    st.write(response.choices[0].message.content)
