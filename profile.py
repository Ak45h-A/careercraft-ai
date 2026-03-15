import streamlit as st
import json

def render():
    st.markdown('<h1>👤 My Profile</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Fill this once — reused everywhere across resumes, applications & biodata</p>', unsafe_allow_html=True)

    p = st.session_state.profile

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Personal", "Experience", "Education", "Skills", "Links & Others"])

    with tab1:
        st.markdown('<div class="step-header">Personal Information</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            p["name"] = st.text_input("Full Name *", value=p.get("name", ""), placeholder="e.g. Rahul Sharma")
            p["email"] = st.text_input("Email *", value=p.get("email", ""), placeholder="rahul@email.com")
            p["phone"] = st.text_input("Phone *", value=p.get("phone", ""), placeholder="+91 9876543210")
            p["city"] = st.text_input("City", value=p.get("city", ""), placeholder="Bengaluru")
            p["state"] = st.text_input("State", value=p.get("state", ""), placeholder="Karnataka")
        with col2:
            p["dob"] = st.text_input("Date of Birth", value=p.get("dob", ""), placeholder="01 Jan 1995")
            p["gender"] = st.selectbox("Gender", ["Prefer not to say", "Male", "Female", "Other"],
                index=["Prefer not to say","Male","Female","Other"].index(p.get("gender","Prefer not to say")))
            p["nationality"] = st.text_input("Nationality", value=p.get("nationality", "Indian"))
            p["languages"] = st.text_input("Languages Known", value=p.get("languages", ""), placeholder="English, Hindi, Kannada")
            p["summary"] = st.text_area("Professional Summary", value=p.get("summary", ""),
                placeholder="Brief 3-4 line summary about yourself and career goals...", height=100)

    with tab2:
        st.markdown('<div class="step-header">Work Experience</div>', unsafe_allow_html=True)
        st.markdown("""<div class="tip-box">💡 Add each job separately. Most recent first.</div>""", unsafe_allow_html=True)

        if "experiences" not in p:
            p["experiences"] = [{}]

        num_exp = st.number_input("Number of jobs", min_value=0, max_value=10, value=max(1, len(p["experiences"])))
        while len(p["experiences"]) < num_exp:
            p["experiences"].append({})
        while len(p["experiences"]) > num_exp:
            p["experiences"].pop()

        for i in range(int(num_exp)):
            with st.expander(f"Job {i+1}: {p['experiences'][i].get('title', 'Untitled')} @ {p['experiences'][i].get('company', '—')}", expanded=(i==0)):
                exp = p["experiences"][i]
                c1, c2 = st.columns(2)
                with c1:
                    exp["title"] = st.text_input("Job Title", value=exp.get("title",""), key=f"exp_title_{i}", placeholder="Software Engineer")
                    exp["company"] = st.text_input("Company", value=exp.get("company",""), key=f"exp_co_{i}", placeholder="TCS")
                    exp["location"] = st.text_input("Location", value=exp.get("location",""), key=f"exp_loc_{i}", placeholder="Bengaluru")
                with c2:
                    exp["start"] = st.text_input("Start Date", value=exp.get("start",""), key=f"exp_start_{i}", placeholder="Jan 2021")
                    exp["end"] = st.text_input("End Date (or 'Present')", value=exp.get("end",""), key=f"exp_end_{i}", placeholder="Present")
                    exp["type"] = st.selectbox("Type", ["Full-time","Part-time","Internship","Contract","Freelance"],
                        key=f"exp_type_{i}")
                exp["description"] = st.text_area("Achievements & Responsibilities",
                    value=exp.get("description",""), key=f"exp_desc_{i}",
                    placeholder="• Developed REST APIs using Python/Django\n• Reduced load time by 40%\n• Led team of 4 engineers",
                    height=120)

    with tab3:
        st.markdown('<div class="step-header">Education</div>', unsafe_allow_html=True)

        if "education" not in p:
            p["education"] = [{}]

        num_edu = st.number_input("Number of degrees", min_value=1, max_value=6, value=max(1, len(p["education"])))
        while len(p["education"]) < num_edu:
            p["education"].append({})

        for i in range(int(num_edu)):
            with st.expander(f"Degree {i+1}: {p['education'][i].get('degree','Untitled')}", expanded=(i==0)):
                edu = p["education"][i]
                c1, c2 = st.columns(2)
                with c1:
                    edu["degree"] = st.text_input("Degree/Certificate", value=edu.get("degree",""), key=f"edu_deg_{i}", placeholder="B.E. Computer Science")
                    edu["institution"] = st.text_input("Institution", value=edu.get("institution",""), key=f"edu_inst_{i}", placeholder="VTU Bengaluru")
                with c2:
                    edu["year"] = st.text_input("Year", value=edu.get("year",""), key=f"edu_yr_{i}", placeholder="2017 - 2021")
                    edu["grade"] = st.text_input("CGPA / Percentage", value=edu.get("grade",""), key=f"edu_gr_{i}", placeholder="8.5 CGPA")

    with tab4:
        st.markdown('<div class="step-header">Skills & Expertise</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            p["technical_skills"] = st.text_area("Technical Skills",
                value=p.get("technical_skills",""),
                placeholder="Python, Java, React, Node.js, SQL, AWS, Docker, Git",
                height=100)
            p["tools"] = st.text_area("Tools & Platforms",
                value=p.get("tools",""),
                placeholder="VS Code, Jira, Postman, Figma, Linux",
                height=80)
        with col2:
            p["soft_skills"] = st.text_area("Soft Skills",
                value=p.get("soft_skills",""),
                placeholder="Leadership, Communication, Problem Solving, Teamwork",
                height=100)
            p["certifications"] = st.text_area("Certifications",
                value=p.get("certifications",""),
                placeholder="AWS Certified Developer, Google Cloud Fundamentals",
                height=80)
        p["projects"] = st.text_area("Key Projects",
            value=p.get("projects",""),
            placeholder="1. E-commerce App (React + Node): Built a full-stack app with 500+ users\n2. ML Classifier: 92% accuracy for spam detection",
            height=120)

    with tab5:
        st.markdown('<div class="step-header">Links & Additional</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            p["linkedin"] = st.text_input("LinkedIn URL", value=p.get("linkedin",""), placeholder="linkedin.com/in/yourname")
            p["github"] = st.text_input("GitHub URL", value=p.get("github",""), placeholder="github.com/yourname")
            p["portfolio"] = st.text_input("Portfolio / Website", value=p.get("portfolio",""), placeholder="yourname.dev")
        with col2:
            p["expected_salary"] = st.text_input("Expected Salary (CTC)", value=p.get("expected_salary",""), placeholder="12 LPA")
            p["notice_period"] = st.text_input("Notice Period", value=p.get("notice_period",""), placeholder="30 days / Immediate")
            p["total_experience"] = st.text_input("Total Experience", value=p.get("total_experience",""), placeholder="3 years 2 months")

        p["hobbies"] = st.text_input("Hobbies / Interests", value=p.get("hobbies",""), placeholder="Photography, Open Source, Trekking")
        p["achievements"] = st.text_area("Achievements & Awards",
            value=p.get("achievements",""),
            placeholder="• Best Performer Award - TCS 2023\n• Hackathon Winner - HackIndia 2022",
            height=80)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,2])
    with col1:
        if st.button("💾 Save Profile", use_container_width=True):
            st.session_state.profile = p
            st.success("✅ Profile saved successfully!")
    with col2:
        if st.button("🗑️ Clear All", use_container_width=True):
            st.session_state.profile = {}
            st.rerun()

    if p.get("name"):
        st.markdown(f"""
        <div class="success-box">
            ✅ Profile saved for <strong>{p.get('name')}</strong> — 
            {len(p.get('experiences', []))} job(s), {len(p.get('education', []))} degree(s)
        </div>
        """, unsafe_allow_html=True)
