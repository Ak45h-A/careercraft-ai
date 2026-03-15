import streamlit as st

def render():
    st.markdown('<div class="main-title">CareerCraft AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Build ATS-optimized resumes, ace job applications & create stunning biodatas — powered by AI</div>', unsafe_allow_html=True)

    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<div class="stat-box"><div class="number">ATS</div><div class="label">Resume Optimizer</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="stat-box"><div class="number">AI</div><div class="label">Q&A Generator</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="stat-box"><div class="number">3+</div><div class="label">Job Platforms</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="stat-box"><div class="number">PDF</div><div class="label">+ DOCX + HTML</div></div>""", unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("### 🚀 Quick Start")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>👤 Step 1 — Build Your Profile</h3>
            <p>Enter your personal details, skills, experience & education once. Everything else is auto-filled.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to My Profile →", key="home_profile"):
            st.session_state.page = "profile"
            st.rerun()

        st.markdown("""
        <div class="feature-card">
            <h3>📄 Step 2 — Generate ATS Resume</h3>
            <p>Paste any job description. AI tailors your resume with matching keywords and ATS score.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Build Resume →", key="home_resume"):
            st.session_state.page = "resume"
            st.rerun()

        st.markdown("""
        <div class="feature-card">
            <h3>🎨 Step 3 — Pick a Template</h3>
            <p>Choose from beautiful Canva-style templates. Customize colors, fonts, layouts.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Browse Templates →", key="home_templates"):
            st.session_state.page = "templates"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>💼 Job Application Assistant</h3>
            <p>Auto-generate cover letters & answers to common application questions for LinkedIn, Naukri & Indeed.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Apply to Jobs →", key="home_jobs"):
            st.session_state.page = "jobs"
            st.rerun()

        st.markdown("""
        <div class="feature-card">
            <h3>💬 Interview Q&A Generator</h3>
            <p>AI-crafts personalized answers to "Why should we hire you?", "Tell me about yourself" & more.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Prep Interview →", key="home_qa"):
            st.session_state.page = "qa"
            st.rerun()

        st.markdown("""
        <div class="feature-card">
            <h3>💒 Marriage Biodata Creator</h3>
            <p>Generate a beautiful, traditional or modern marriage biodata with photo, family & personal details.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Create Biodata →", key="home_biodata"):
            st.session_state.page = "biodata"
            st.rerun()

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Checklist
    profile_done = bool(st.session_state.profile.get("name"))
    api_done = bool(st.session_state.api_key)

    st.markdown("### 📋 Setup Checklist")
    col1, col2, col3 = st.columns(3)
    with col1:
        icon = "✅" if profile_done else "⭕"
        st.markdown(f"""<div class="stat-box"><div style='font-size:1.8rem'>{icon}</div><div class="label">Profile Created</div></div>""", unsafe_allow_html=True)
    with col2:
        icon = "✅" if api_done else "⭕"
        st.markdown(f"""<div class="stat-box"><div style='font-size:1.8rem'>{icon}</div><div class="label">AI API Connected</div></div>""", unsafe_allow_html=True)
    with col3:
        resume_done = bool(st.session_state.generated_resume)
        icon = "✅" if resume_done else "⭕"
        st.markdown(f"""<div class="stat-box"><div style='font-size:1.8rem'>{icon}</div><div class="label">Resume Generated</div></div>""", unsafe_allow_html=True)

    if not api_done or not profile_done:
        st.markdown("""
        <div class="tip-box">
            💡 <strong>Get Started:</strong> First go to <strong>Settings</strong> to add your Anthropic API key, then fill in <strong>My Profile</strong>. 
            After that, all AI features will work automatically!
        </div>
        """, unsafe_allow_html=True)
