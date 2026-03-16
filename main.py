from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def prompt(resume_text, jd_text):
    prompt_template = ChatPromptTemplate.from_template(
        '''
you are an expert career consultant. Compare the following resume and job description.

Resume:
{resume}

Jobdescription:
{jd}

analyse and provide a structured JSON response with the following fields:
1.Job Title Match: Describe how well the job title aligns
2.Roles and Responsibilities: see if the candidate's duties align with the job requirements
3.Years of Experience:verify if the candidate meet the required experience
4.Keyword Match:identify whether key JD skills appear in the resume 
5.Overall Match Score:give a score showing the overall alignment.
6.Summary Fit:write a brief summary 
7.Suggestions:The candidate should consider acquiring more experience in machine learning engineering or related fields.

return your result in valid JSON format only.
You MUST output ONLY a valid JSON object.

Follow these rules strictly:
1. ALWAYS wrap all text values in quotes.
2. NEVER write comments inside JSON.
3. NEVER write anything outside the JSON object.
4. NEVER use unquoted text.
5. Numbers must be plain integers when appropriate.
6. DO NOT include markdown or explanations.
7. Arrays must contain ONLY strings.
8. If something is missing, use "" or [].
9. Do NOT invent keys — ONLY use the schema below.

### JSON Schema (FOLLOW EXACTLY):

{{ 
    "Job Title Match": "string",
    "Roles and Responsibilities": {{
        "Alignments": ["string"],
        "Mismatches": ["string"]
    }},
    "Years of Experience": {{
        "Required": "string",
        "Candidate": "string"
    }},
    "Keyword Match": ["string"],
    "Overall Match Score": 0,
    "Summary Fit": "string",
    "Suggestions": "string"
}}

### NOW OUTPUT ONLY THE JSON.
'''
    )  

    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.1
    )

    parser = StrOutputParser()
    chain = prompt_template | llm | parser

    response = chain.invoke({
        "resume": resume_text,
        "jd": jd_text
    })

    print(response)
    return response
