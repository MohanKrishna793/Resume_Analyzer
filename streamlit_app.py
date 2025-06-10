import streamlit as st
import PyPDF2
import docx2txt
import re

# --- Define job roles and their required skills ---
JOB_ROLES = {
    "Data Scientist": {"python", "pandas", "numpy", "scikit-learn", "matplotlib", "machine learning", "statistics", "sql", "git"},
    "Web Developer": {"html", "css", "javascript", "react", "node.js", "express", "mongodb", "git"},
    "Cloud Engineer": {"aws", "azure", "gcp", "docker", "kubernetes", "linux", "terraform", "ci/cd", "git"},
}

ALL_SKILLS = set().union(*JOB_ROLES.values())

# --- Skill extraction using regex-based keyword search ---
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    found_skills = set()
    for skill in ALL_SKILLS:
        # Word boundary for precise matching
        if re.search(r"\b" + re.escape(skill.lower()) + r"\b", resume_text):
            found_skills.add(skill)
    return found_skills

def match_job_role(user_skills):
    best_role = None
    best_match_count = 0
    match_details = {}
    for role, role_skills in JOB_ROLES.items():
        matched = user_skills & role_skills
        match_details[role] = len(matched)
        if len(matched) > best_match_count:
            best_match_count = len(matched)
            best_role = role
    return best_role, match_details

# --- Streamlit App ---
st.title("🧠 Resume Analyzer & Smart Job Recommender")
st.write("Upload your resume (PDF or DOCX) to see your best job fit and skill recommendations.")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    filetype = uploaded_file.name.split(".")[-1].lower()
    if filetype == "pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    elif filetype == "docx":
        resume_text = extract_text_from_docx(uploaded_file)
    else:
        st.error("Unsupported file type.")
        st.stop()

    with st.expander("See extracted resume text (for debugging)", expanded=False):
        st.write(resume_text)

    user_skills = extract_skills(resume_text)
    st.subheader("🗂️ Extracted Skills")
    if user_skills:
        st.write(", ".join(sorted(user_skills)))
    else:
        st.write("No relevant skills found. Please check your resume.")

    best_role, match_details = match_job_role(user_skills)

    # Show match breakdown for all roles
    st.subheader("🚀 Job Role Match Overview")
    for role, skills in JOB_ROLES.items():
        matched_skills = user_skills & skills
        missing_skills = skills - user_skills
        st.markdown(f"**{role}**")
        st.write(f"- Matched Skills: {', '.join(sorted(matched_skills)) if matched_skills else 'None'}")
        st.write(f"- Missing Skills: {', '.join(sorted(missing_skills)) if missing_skills else 'None'}")
        st.progress(len(matched_skills) / len(skills))

    # Recommendation
    if best_role:
        st.header(f"🎯 Best Matched Role: {best_role}")
        matched = user_skills & JOB_ROLES[best_role]
        missing = JOB_ROLES[best_role] - user_skills
        st.write(f"**Matched Skills:** {', '.join(sorted(matched)) if matched else 'None'}")
        st.write(f"**Skill Gaps:** {', '.join(sorted(missing)) if missing else 'None'}")
        if missing:
            st.info(f"To improve your fit for {best_role}, consider learning: {', '.join(sorted(missing))}")
        else:
            st.success(f"Excellent! You have all the key skills for {best_role}.")
    else:
        st.warning("No strong job role match found based on the extracted skills.")
