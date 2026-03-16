import streamlit as st
from PyPDF2 import PdfReader
from main import prompt

st.set_page_config(page_title="RESUME",layout="centered")
st.title("Resume Parser")
st.markdown('''
            Upload your Job Description here
            Paste your Resume here
            ''')

def extract_text(file):
    reader=PdfReader(file)
    text=""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
    
resume_text=st.text_area("Paste your resume text here!",height=250)
jd_file=st.file_uploader("upload your jd here",type=["pdf","txt","docx"])

jd_text=""
if jd_file:
    if jd_file.type=="application/pdf":
        jd_text=extract_text(jd_file)
    else:
        jd_text=jd_file.read().decode("utf-8")
        
        
if st.button("Submit"):
    if not resume_text.strip() or not jd_text.strip():
        st.warning("File doesnot exists")
    else:
        with st.spinner("loading"):
            try:
                response=prompt(resume_text,jd_text)
                st.subheader("here is your result")
                st.json(response)
            except Exception as e:
                st.error(e)
        
        
    