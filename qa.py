import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ai_helper import call_ai, profile_to_text

COMMON_QUESTIONS = [
    "Tell me about yourself",
    "Why should we hire you?",
    "What are your strengths and weaknesses?",
    "Why do you want to work at this company?",
    "Where do you see yourself in 5 years?",
    "Why are you leaving your current job?",
    "What is your greatest achievement?",
    "Describe a challenge you faced and how you overcame it",
    "How do you handle pressure and tight deadlines?",
    "What motivates you?",
    "Are you a team player or prefer working alone?",
    "What salary do you expect?",
    "Do you have any questions for us?",
]

def render():
    st.markdown('<h1>💬 Interview Q&A Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">AI-crafted personalized answers to every interview question</p>', unsafe_allow_html=True)

    p = st.session_state.profile
    if not p.get("name"):
        st.markdown("""<div class="tip-box">⚠️ Please fill in your profile first.</div>""", unsafe_allow_html=True)
        return

    tab1, tab2, tab3 = st.tabs(["🎯 Common Questions", "✏️ Custom Question", "🔥 Mock Interview"])

    with tab1:
        st.markdown('<div class="step-header">Common Interview Questions</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            qa_role = st.text_input("Target Role", placeholder="Software Engineer at Flipkart")
            qa_company = st.text_input("Company", placeholder="Flipkart")
        with col2:
            qa_level = st.selectbox("Seniority Level", ["Fresher", "Junior (1-3 yrs)", "Mid (3-6 yrs)", "Senior (6+ yrs)", "Lead/Manager"])
            qa_style = st.selectbox("Answer Style", ["STAR Method", "Concise & Direct", "Storytelling", "Data-driven"])

        st.markdown("**Select Questions:**")
        selected_qs = []
        cols = st.columns(2)
        for i, q in enumerate(COMMON_QUESTIONS):
            with cols[i % 2]:
                if st.checkbox(q, key=f"q_{i}"):
                    selected_qs.append(q)

        if st.button("💬 Generate All Answers", use_container_width=True):
            if not selected_qs:
                st.warning("Select at least one question.")
            else:
                with st.spinner("Preparing your personalized answers..."):
                    profile_text = profile_to_text(p)
                    all_qs = "\n".join([f"{i+1}. {q}" for i, q in enumerate(selected_qs)])
                    prompt = f"""
You are an expert interview coach. Generate personalized, compelling answers for these interview questions.

Candidate: {p.get('name','')}
Role: {qa_role}
Company: {qa_company}
Level: {qa_level}
Answer Style: {qa_style}

PROFILE:
{profile_text}

QUESTIONS:
{all_qs}

For each question:
- Use {qa_style} approach
- Reference specific experiences, numbers, and achievements from the profile
- Keep answers authentic and human, not robotic
- Format as: **Q: [question]**\n**A:** [answer]\n\n
"""
                    result = call_ai(prompt, max_tokens=3000)
                    st.session_state["qa_answers"] = result

        if st.session_state.get("qa_answers"):
            st.markdown("<hr class='divider'>", unsafe_allow_html=True)
            st.markdown(st.session_state["qa_answers"])
            st.download_button("📥 Download All Answers", data=st.session_state["qa_answers"],
                file_name="interview_answers.txt", mime="text/plain")

    with tab2:
        st.markdown('<div class="step-header">Custom Question Answerer</div>', unsafe_allow_html=True)
        custom_role = st.text_input("Role/Context", key="cq_role", placeholder="Data Scientist at Amazon")
        custom_q = st.text_area("Your Question", key="cq_q", height=100,
            placeholder="e.g. You have a gap in your resume. Can you explain that?\nor\nWhy do you want to transition from marketing to tech?")

        if st.button("🎯 Answer This Question", use_container_width=True, key="custom_qa_btn"):
            if custom_q:
                with st.spinner("Crafting your answer..."):
                    profile_text = profile_to_text(p)
                    result = call_ai(f"""
Answer this interview question for the candidate.

Role: {custom_role}
Question: {custom_q}

Candidate Profile:
{profile_text}

Provide:
1. A primary answer (STAR method if applicable, ~200 words)
2. A shorter alternative answer (~100 words)
3. 2-3 tips to deliver this answer confidently
""", max_tokens=800)
                    st.markdown(result)
            else:
                st.warning("Please type a question first.")

    with tab3:
        st.markdown('<div class="step-header">🔥 Mock Interview Simulator</div>', unsafe_allow_html=True)
        st.markdown("""<div class="tip-box">Type your answer to a random interview question. AI will evaluate it and give feedback!</div>""", unsafe_allow_html=True)

        mock_role = st.text_input("Role to practice for", key="mock_role", placeholder="Full Stack Developer")

        if st.button("🎲 Give Me a Random Question", use_container_width=True):
            import random
            q = random.choice(COMMON_QUESTIONS)
            st.session_state["mock_question"] = q

        if st.session_state.get("mock_question"):
            st.markdown(f"""
            <div class="feature-card" style="border-color:#6c63ff;">
                <h3>🎤 Interview Question:</h3>
                <p style="font-size:1.1rem; color:#f0f0f5; margin-top:8px;">"{st.session_state['mock_question']}"</p>
            </div>
            """, unsafe_allow_html=True)

            mock_answer = st.text_area("Your Answer:", key="mock_ans", height=150, placeholder="Type your answer here as if you're in the interview...")

            if st.button("📊 Evaluate My Answer", use_container_width=True):
                if mock_answer:
                    with st.spinner("Evaluating..."):
                        profile_text = profile_to_text(p)
                        result = call_ai(f"""
Evaluate this interview answer and provide coaching feedback.

Role: {mock_role}
Question: {st.session_state['mock_question']}
Candidate's Answer: {mock_answer}

Candidate Profile: {profile_text}

Provide:
1. Overall Score (0-10) with brief reasoning
2. What worked well (2-3 points)
3. What to improve (2-3 points)
4. A better version of their answer
5. One-line delivery tip

Be constructive and encouraging.
""", max_tokens=800)
                        st.markdown(result)
