# 🧠 ResumeInsight Project Plan Report

## 👥 1.1. Team Information

**👨‍💻 Team Name:** **JobGenie**

**👨‍👩‍👦‍👦 Team Members & Roles:**

- 🧑‍✈️ **U. Mohan Krishna Reddy** – *Team Lead*  
  📌 Oversees coordination, task allocation, progress tracking, and decision-making.

- 🤖 **K. Subhash** – *AI Engineer*  
  🛠️ Integrates semantic search & GPT-4o using prompt engineering & optimization.

- 🎨 **M. Anirudh** – *Frontend / UI-UX Developer*  
  🖥️ Designs UI in Streamlit, handles session state, and interactive visualizations.

- 📊 **M. Yuva Kishore** – *Data Scientist & Tester*  
  🔍 Builds parsing pipeline, preprocesses data, and tests AI quality.

- 📄 **M. Srichakra Kanwa** – *Documentation & Deployment Lead*  
  📝 Manages docs, README, deployment on Hugging Face Spaces & CI/CD.

---

## 📄 1.2. Application Overview

**🧾 Application Name:** *Resume Analyzer & Job Recommender*

**🔍 Use Case & Problem Solved:**  
Many struggle to align resumes with real job demands or identify what to learn next.  
**ResumeInsight** parses resumes, matches jobs, shows skill gaps, and offers career advice using AI.

👤 *Target Users:* Students, job seekers, and career switchers.

**✨ Key Features:**

- 📄 Resume parsing (skills, education, experience)
- 🧠 AI-driven job recommendations (semantic similarity)
- 📈 Skill gap radar charts
- 💬 GPT-powered career tips & upskilling roadmap
- 🧾 Downloadable PDF report

**🎯 Motivation:**  
Job seekers lack direction on resume-job alignment and skill development. Our AI tool fills this gap with smart guidance.

---

## 🤖 1.3. AI Integration Details

**🧠 AI Models Planned:**

- 🧬 `all-MiniLM-L6-v2` (semantic similarity via Sentence Transformers)
- 🧠 GPT-4o (career tips & advice)
- 🧾 SpaCy (NER for resumes)

**🔌 AI Integration Flow:**

1. 📑 Parse resume → extract structured info
2. 📊 Encode & match with job descriptions
3. 📉 Identify skill gaps
4. 💡 GPT-4o gives learning suggestions

**🧪 Sample Prompts:**

- “🧑‍🏫 *Act as a career coach for a graduate applying to {role}.*”
- “📘 *Given skills: {skills} vs required: {jd_skills}, suggest a learning roadmap.*”

---

## 🏗️ 1.4. Technical Architecture & Development

**🖼️ Architecture Diagram:** *(To be added post-deployment)*

**🧰 Tech Stack:**

- 🎛️ Frontend: **Streamlit**
- 🧠 Backend: **FastAPI**
- 🤖 AI: **Transformers + GPT-4o**
- 🗃️ Database: **MySQL**
- 🧭 Semantic Search: **FAISS** or **scikit-learn 
- 🚀 Deployment: **GitLab CI/CD + HF Spaces**


**⚠️ Challenges & Fixes:**

- 📄 Parsing noise → Hybrid PDFMiner + heuristics
- 🚦 API rate limits → Redis caching
- 💾 HF size limits → Quantized models + lazy loading

**📜 License:** MIT License

---

## 🧪 1.5. User Testing & Feedback

**📐 Methodology:**  
🔁 Share app with 10–12 users  
📊 Feedback via Google Form (Likert + short answer)

**👥 Test Group:** Final-year students, graduates, mentors  
🎯 Goals: Test UX, clarity, relevance, GPT feedback

**🔄 Iteration Plan:**

- 📤 Export skill gap to CSV
- 📱 Simplify radar chart for mobile
- 💬 Rework GPT prompt clarity

---

## 🚀 1.6. Future Roadmap & User Adoption

### ⏩ **Phase-wise Development Plan**

**📅 Phase 1 (Weeks 1–2):**  
- 🎨 Polish UI  
- 📄 Improve resume parsing  
- 📝 Add feedback form

**📅 Phase 2 (Weeks 3–4):**  
- 🔗 Add LinkedIn integration  
- 🌐 Support for Hindi resumes

**📅 Phase 3 (Weeks 5–6):**  
- 🧩 Plugin support (custom skill maps)  
- 🔓 Public API for job matching

---

### 🎯 User Adoption Plan

**👥 Target Audience:**  
- 🧑‍🎓 Students  
- 🔄 Career Switchers  
- 🆕 Freshers  
- 👨‍💼 Early Professionals

**💎 Value Delivered:**

- 📊 Skill Gap Map  
- 🧠 Instant Role Matching  
- 🧭 GPT Tips for Upskilling

**📢 Promotion Channels:**

- 🌐 Hugging Face Spaces  
- 💼 LinkedIn, X (formerly Twitter)  
- 🌟 Streamlit Forum  
- 📽️ Video demos & carousels

**🚪 Onboarding Strategy:**

- 🧾 Preloaded sample resume  
- 👣 Guided walk-through  
- ❓ FAQ on each section

---

### 📬 Feedback Loop & Community

- 📋 Google Form with comments/ratings  
- 👍👎 Feedback on GPT output  
- 🤝 Contributing guidelines (`CONTRIBUTING.md`)  
- 🆕 Feature requests via GitLab issues  
- 📝 Public changelog + 🎖️ Contributor badge
