# ai_engine.py
from openai import OpenAI

def analyze_request(request_text, api_key):

    client = OpenAI(api_key=api_key)

    prompt = f"""
    You are a senior business analyst in asset management.

    Convert this request into:

    1 Functional Requirements
    2 Non Functional Requirements
    3 User Stories
    4 Architecture Suggestions

    Request:
    {request_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": prompt}],
        temperature=0.2
    )

    # new SDK returns message in response.choices[0].message.content
    return response.choices[0].message.content