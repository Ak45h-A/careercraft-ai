import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ai_helper import call_ai, profile_to_text

def render():
    st.markdown('<h1>💼 Job Application Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Auto-generate cover letters & application answers for LinkedIn, Naukri & Indeed</p>', unsafe_allow_html=True)

    p = st.session_state.profile
    if not p.get("name"):
        st.markdown("""<div class="tip-box">⚠️ Please fill in <strong>My Profile</strong> first.</div>""", unsafe_allow_html=True)
        return

    tab1, tab2, tab3, tab4 = st.tabs(["📝 Cover Letter", "🤖 Application Q&A", "🔗 Platform Guide", "📋 Application Tracker"])

    with tab1:
        st.markdown('<div class="step-header">Cover Letter Generator</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            cl_job = st.text_input("Job Title", placeholder="Senior Software Engineer")
            cl_company = st.text_input("Company Name", placeholder="Google")
            cl_platform = st.selectbox("Platform", ["LinkedIn", "Naukri.com", "Indeed", "Direct Email", "Other"])
            cl_tone = st.selectbox("Tone", ["Professional & Formal", "Enthusiastic & Energetic", "Concise & Punchy", "Storytelling Style"])
            cl_length = st.selectbox("Length", ["Short (150 words)", "Medium (250 words)", "Detailed (400 words)"])
        with col2:
            cl_jd = st.text_area("Paste Job Description", height=200, placeholder="Optional but recommended for better tailoring...")
            cl_custom = st.text_input("Anything specific to highlight?", placeholder="e.g. My AWS experience, my startup background")

        if st.button("✍️ Generate Cover Letter", use_container_width=True):
            if not cl_job:
                st.error("Enter job title.")
            else:
                with st.spinner("Writing your cover letter..."):
                    profile_text = profile_to_text(p)
                    prompt = f"""
Write a compelling cover letter for a job application.

Platform: {cl_platform}
Job Title: {cl_job}
Company: {cl_company}
Tone: {cl_tone}
Length: {cl_length}
Special focus: {cl_custom}

JOB DESCRIPTION:
{cl_jd or 'Not provided'}

CANDIDATE PROFILE:
{profile_text}

Write a personalized, non-generic cover letter. Do NOT use clichés like "I am writing to express my interest".
Start with a strong hook. Highlight 2-3 specific achievements. End with a confident call to action.
For {cl_platform}, format appropriately (short paragraph for LinkedIn message, full letter for email/others).
"""
                    result = call_ai(prompt, max_tokens=1000)
                    st.session_state["cover_letter"] = result

        if st.session_state.get("cover_letter"):
            st.markdown("<hr class='divider'>", unsafe_allow_html=True)
            st.markdown("**Your Cover Letter:**")
            st.text_area("Cover Letter", value=st.session_state["cover_letter"], height=300)
            st.download_button("📥 Download Cover Letter", data=st.session_state["cover_letter"],
                file_name="cover_letter.txt", mime="text/plain")

    with tab2:
        st.markdown('<div class="step-header">Application Question Answerer</div>', unsafe_allow_html=True)
        st.markdown("""<div class="tip-box">Many job applications ask custom questions. Paste them below and AI will craft personalized answers.</div>""", unsafe_allow_html=True)

        qa_job = st.text_input("Job Title", key="qa_job", placeholder="Data Analyst at Zomato")
        qa_jd = st.text_area("Job Description (Optional)", key="qa_jd", height=120, placeholder="Paste JD for better context...")

        st.markdown("**Application Questions:**")
        questions = []
        for i in range(1, 6):
            q = st.text_input(f"Question {i}", key=f"appq_{i}", placeholder=f"e.g. Why do you want to work at this company?" if i == 1 else "")
            if q.strip():
                questions.append(q)

        if st.button("💬 Generate Answers", use_container_width=True):
            if questions:
                with st.spinner("Generating tailored answers..."):
                    profile_text = profile_to_text(p)
                    all_questions = "\n".join([f"{i+1}. {q}" for i, q in enumerate(questions)])
                    prompt = f"""
You are helping a job applicant answer application questions.

Job: {qa_job}
JD: {qa_jd or 'Not provided'}

Candidate Profile:
{profile_text}

Questions to answer:
{all_questions}

For each question:
- Write a concise, specific, compelling answer
- Reference actual details from the candidate's profile
- Keep each answer under 150 words unless the question requires more
- Make them sound human, not generic

Format: Q1: [question]\nA1: [answer]\n\nQ2: ...
"""
                    result = call_ai(prompt, max_tokens=2000)
                    st.session_state["app_answers"] = result
            else:
                st.warning("Add at least one question.")

        if st.session_state.get("app_answers"):
            st.markdown("<hr class='divider'>", unsafe_allow_html=True)
            st.markdown(st.session_state["app_answers"])
            st.download_button("📥 Download Answers", data=st.session_state["app_answers"],
                file_name="application_answers.txt", mime="text/plain")

    with tab3:
        st.markdown('<div class="step-header">Platform Application Guide</div>', unsafe_allow_html=True)

        platform = st.selectbox("Select Platform", ["LinkedIn", "Naukri.com", "Indeed"])

        if platform == "LinkedIn":
            st.markdown("""
            <div class="feature-card">
                <h3>🔵 LinkedIn Easy Apply Guide</h3>
                <p><strong>Profile Optimization:</strong></p>
                <ul style="margin-top:8px; color:#9090aa; font-size:0.9rem; padding-left:1rem;">
                    <li>Use the exact job title as your headline</li>
                    <li>Add all keywords from your target JDs in skills section</li>
                    <li>Get 5+ recommendations</li>
                    <li>Set "Open to Work" for your target roles</li>
                </ul>
                <p style="margin-top:12px;"><strong>Apply Tips:</strong></p>
                <ul style="color:#9090aa; font-size:0.9rem; padding-left:1rem;">
                    <li>Use Easy Apply with a tailored note</li>
                    <li>Connect with the recruiter first</li>
                    <li>Apply within 24 hours of posting</li>
                    <li>Follow up after 5-7 days</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        elif platform == "Naukri.com":
            st.markdown("""
            <div class="feature-card">
                <h3>🟠 Naukri.com Application Guide</h3>
                <ul style="margin-top:8px; color:#9090aa; font-size:0.9rem; padding-left:1rem;">
                    <li>Update your profile every 2-3 days (boosts visibility)</li>
                    <li>Add 10+ key skills from your domain</li>
                    <li>Keep your resume "freshness" score high</li>
                    <li>Use Naukri's "Resume Score" tool for optimization</li>
                    <li>Apply to jobs posted within 7 days for better response rate</li>
                    <li>Attach a tailored cover letter</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        elif platform == "Indeed":
            st.markdown("""
            <div class="feature-card">
                <h3>🔵 Indeed Application Guide</h3>
                <ul style="margin-top:8px; color:#9090aa; font-size:0.9rem; padding-left:1rem;">
                    <li>Upload your resume once, Indeed auto-fills applications</li>
                    <li>Set up job alerts for instant notifications</li>
                    <li>Use Indeed's Resume Builder for ATS-friendly format</li>
                    <li>Apply to "Easily Apply" jobs for faster process</li>
                    <li>Check company reviews before applying</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        if st.button(f"📋 Generate {platform} Application Strategy", use_container_width=True):
            with st.spinner(f"Creating your {platform} strategy..."):
                profile_text = profile_to_text(p)
                result = call_ai(f"""
Create a personalized {platform} job application strategy for this candidate.
Include: profile optimization tips, search strategy, application approach, follow-up plan.

{profile_text}
""", max_tokens=800)
                st.markdown(result)

    with tab4:
        st.markdown('<div class="step-header">Application Tracker</div>', unsafe_allow_html=True)

        if "applications" not in st.session_state:
            st.session_state.applications = []

        with st.expander("➕ Add New Application", expanded=False):
            col1, col2, col3 = st.columns(3)
            with col1:
                app_company = st.text_input("Company", key="track_co")
                app_role = st.text_input("Role", key="track_role")
            with col2:
                app_platform = st.selectbox("Platform", ["LinkedIn", "Naukri", "Indeed", "Direct", "Referral"], key="track_plat")
                app_status = st.selectbox("Status", ["Applied", "Screening", "Interview", "Offer", "Rejected"], key="track_status")
            with col3:
                app_date = st.text_input("Applied Date", key="track_date", placeholder="15 Mar 2025")
                app_notes = st.text_input("Notes", key="track_notes", placeholder="Follow up by...")

            if st.button("Add to Tracker"):
                st.session_state.applications.append({
                    "company": app_company,
                    "role": app_role,
                    "platform": app_platform,
                    "status": app_status,
                    "date": app_date,
                    "notes": app_notes
                })
                st.success("Added!")
                st.rerun()

        if st.session_state.applications:
            st.markdown("**Your Applications:**")
            for i, app in enumerate(st.session_state.applications):
                status_colors = {
                    "Applied": "#6c63ff", "Screening": "#f59e0b",
                    "Interview": "#3b82f6", "Offer": "#10b981", "Rejected": "#ef4444"
                }
                color = status_colors.get(app["status"], "#888")
                col1, col2 = st.columns([5,1])
                with col1:
                    st.markdown(f"""
                    <div class="feature-card" style="padding:12px;">
                        <strong>{app['company']}</strong> — {app['role']}
                        <span class="badge" style="background:{color}22; color:{color}; border-color:{color}44;">{app['status']}</span>
                        <span class="badge">{app['platform']}</span>
                        <span style="color:#9090aa; font-size:0.8rem; margin-left:8px;">{app['date']}</span>
                        <div style="color:#9090aa; font-size:0.8rem; margin-top:4px;">{app['notes']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    if st.button("🗑️", key=f"del_app_{i}"):
                        st.session_state.applications.pop(i)
                        st.rerun()
        else:
            st.info("No applications tracked yet. Add your first one above!")
