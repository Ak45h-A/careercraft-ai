import streamlit as st

def render():
    st.markdown('<h1>⚙️ Settings</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Configure your API key and app preferences</p>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔑 API Configuration", "🎨 Preferences"])

    with tab1:
        st.markdown('<div class="step-header">Anthropic API Key</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="tip-box">
            🔑 All AI features require an Anthropic API key. Your key is stored only in your session (not saved to disk).
            <br><br>
            Get your API key from: <a href="https://console.anthropic.com" target="_blank" style="color:#6c63ff;">console.anthropic.com</a>
        </div>
        """, unsafe_allow_html=True)

        current_key = st.session_state.get("api_key", "")
        masked = "sk-..." + current_key[-6:] if current_key and len(current_key) > 10 else ""

        if masked:
            st.markdown(f"""
            <div class="success-box">
                ✅ API Key configured: <code>{masked}</code>
            </div>
            """, unsafe_allow_html=True)

        new_key = st.text_input("Enter Anthropic API Key",
            type="password",
            placeholder="sk-ant-api03-...",
            help="Your API key starting with sk-ant-")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save API Key", use_container_width=True):
                if new_key.strip():
                    st.session_state.api_key = new_key.strip()
                    st.success("✅ API Key saved for this session!")
                    st.rerun()
                else:
                    st.error("Please enter a valid API key.")
        with col2:
            if st.button("🔄 Test Connection", use_container_width=True):
                key = new_key.strip() or st.session_state.get("api_key","")
                if key:
                    try:
                        import anthropic
                        client = anthropic.Anthropic(api_key=key)
                        msg = client.messages.create(
                            model="claude-opus-4-5",
                            max_tokens=50,
                            messages=[{"role": "user", "content": "Say 'Connection successful!' only"}]
                        )
                        st.success(f"✅ {msg.content[0].text}")
                    except Exception as e:
                        st.error(f"❌ Connection failed: {str(e)}")
                else:
                    st.warning("Please enter an API key first.")

        if st.button("🗑️ Clear API Key"):
            st.session_state.api_key = ""
            st.success("API Key cleared.")
            st.rerun()

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("### 💡 Free Alternative: Use Ollama (Local AI)")
        st.markdown("""
        <div class="tip-box">
            You can also run this tool completely FREE using local AI (Ollama with Llama 3):
            <br>1. Install Ollama: <code>curl -fsSL https://ollama.com/install.sh | sh</code>
            <br>2. Pull model: <code>ollama pull llama3</code>
            <br>3. Set API Base URL below to: <code>http://localhost:11434</code>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="step-header">App Preferences</div>', unsafe_allow_html=True)

        st.selectbox("Default Resume Tone", ["Professional & Formal", "Technical & Detailed", "Creative & Dynamic"])
        st.selectbox("Default Template", ["modern_purple", "minimal_black", "corporate_blue", "creative_teal"])
        st.number_input("Max AI Output Tokens", min_value=500, max_value=4000, value=2000, step=100)
        st.checkbox("Auto-save profile on changes", value=True)
        st.checkbox("Show ATS tips during resume generation", value=True)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("### 🗄️ Data Management")
        col1, col2 = st.columns(2)
        with col1:
            import json
            profile_json = json.dumps(st.session_state.get("profile", {}), indent=2)
            st.download_button("📥 Export Profile as JSON",
                data=profile_json, file_name="career_profile.json", mime="application/json",
                use_container_width=True)
        with col2:
            uploaded = st.file_uploader("📤 Import Profile JSON", type=["json"])
            if uploaded:
                try:
                    data = json.load(uploaded)
                    st.session_state.profile = data
                    st.success("✅ Profile imported successfully!")
                    st.rerun()
                except:
                    st.error("Invalid JSON file.")

        if st.button("🗑️ Clear All Data", use_container_width=True):
            st.session_state.profile = {}
            st.session_state.generated_resume = None
            st.session_state.biodata = {}
            st.success("All data cleared.")
            st.rerun()
