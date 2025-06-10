import streamlit as st
from resume_parser import parse_resume
from utils import load_job_roles, recommend_job_and_gaps

st.title("Resume Analyzer & Smart Job Recommendation")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    resume_text, user_profile = parse_resume(uploaded_file)
    st.subheader("Extracted Resume Information")
    st.write(user_profile)
    
    job_roles = load_job_roles()
    recommended_job, gaps, matched_skills = recommend_job_and_gaps(user_profile, job_roles)
    
    st.subheader("Best Matching Job Recommendation")
    st.success(f"Recommended Job: {recommended_job['title']}")
    st.write(f"**Job Requirements:** {', '.join(recommended_job['skills'])}")
    st.write(f"**Your Matching Skills:** {', '.join(matched_skills)}")
    
    st.subheader("Skill Gaps & Improvement Suggestions")
    if gaps:
        st.warning("To improve your fit for this job, consider developing these areas:")
        st.write(", ".join(gaps))
    else:
        st.success("You meet all the key requirements for this role!")
