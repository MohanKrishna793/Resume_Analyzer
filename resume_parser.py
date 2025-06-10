import docx2txt
import PyPDF2
import re

def parse_resume(uploaded_file):
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = "".join([page.extract_text() or "" for page in pdf_reader.pages])
    else:
        text = docx2txt.process(uploaded_file)
    user_profile = extract_profile(text)
    return text, user_profile

def extract_profile(text):
    # Simple keyword-based skill extraction
    skills = []
    known_skills = [
        "python", "java", "c++", "sql", "machine learning", "deep learning", "data analysis",
        "pandas", "numpy", "scikit-learn", "tensorflow", "communication", "leadership",
        "project management", "aws", "azure", "docker", "git", "html", "css", "javascript"
    ]
    text_lower = text.lower()
    for skill in known_skills:
        if re.search(rf'\b{skill}\b', text_lower):
            skills.append(skill)
    # (Optional) Add regex to extract education/years/other info
    return {"skills": skills}
