def load_job_roles():
    # This can be replaced with a file or database in a real app
    return [
        {
            "title": "Data Scientist",
            "skills": ["python", "machine learning", "data analysis", "pandas", "numpy", "scikit-learn"]
        },
        {
            "title": "Web Developer",
            "skills": ["html", "css", "javascript", "python", "git"]
        },
        {
            "title": "Cloud Engineer",
            "skills": ["aws", "azure", "docker", "python", "git"]
        },
    ]

def recommend_job_and_gaps(user_profile, job_roles):
    user_skills = set(user_profile.get("skills", []))
    best_match = None
    max_matched = 0
    matched_skills = []
    for job in job_roles:
        job_skills = set(job["skills"])
        matched = user_skills & job_skills
        if len(matched) > max_matched:
            max_matched = len(matched)
            best_match = job
            matched_skills = list(matched)
    gaps = list(set(best_match["skills"]) - user_skills) if best_match else []
    return best_match, gaps, matched_skills
