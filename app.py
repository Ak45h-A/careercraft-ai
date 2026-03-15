import streamlit as st

st.set_page_config(
    page_title="CareerCraft AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Professional Dark Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --bg-primary: #0a0a0f;
    --bg-secondary: #12121a;
    --bg-card: #1a1a2e;
    --accent: #6c63ff;
    --accent2: #ff6584;
    --accent3: #43e97b;
    --text-primary: #f0f0f5;
    --text-secondary: #9090aa;
    --border: #2a2a3e;
    --gradient: linear-gradient(135deg, #6c63ff 0%, #ff6584 100%);
}

* { font-family: 'DM Sans', sans-serif; }

.stApp {
    background: var(--bg-primary);
    color: var(--text-primary);
}

section[data-testid="stSidebar"] {
    background: var(--bg-secondary) !important;
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] .stMarkdown h1,
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 {
    font-family: 'Syne', sans-serif;
    color: var(--text-primary);
}

.main-title {
    font-family: 'Syne', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.2rem;
}

.subtitle {
    color: var(--text-secondary);
    font-size: 1.1rem;
    font-weight: 300;
    margin-bottom: 2rem;
}

.feature-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    transition: all 0.3s ease;
    cursor: pointer;
}

.feature-card:hover {
    border-color: var(--accent);
    box-shadow: 0 0 20px rgba(108, 99, 255, 0.2);
    transform: translateY(-2px);
}

.feature-card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.4rem;
}

.feature-card p {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin: 0;
}

.badge {
    display: inline-block;
    background: rgba(108,99,255,0.15);
    color: var(--accent);
    border: 1px solid rgba(108,99,255,0.4);
    border-radius: 20px;
    padding: 2px 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin: 2px;
}

.badge-green {
    background: rgba(67,233,123,0.15);
    color: var(--accent3);
    border-color: rgba(67,233,123,0.4);
}

.badge-pink {
    background: rgba(255,101,132,0.15);
    color: var(--accent2);
    border-color: rgba(255,101,132,0.4);
}

.stat-box {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
}

.stat-box .number {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-box .label {
    color: var(--text-secondary);
    font-size: 0.85rem;
    margin-top: 4px;
}

div[data-testid="stButton"] button {
    background: var(--gradient);
    color: white;
    border: none;
    border-radius: 10px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    padding: 0.5rem 1.5rem;
    transition: all 0.3s ease;
}

div[data-testid="stButton"] button:hover {
    opacity: 0.85;
    transform: translateY(-1px);
    box-shadow: 0 8px 25px rgba(108,99,255,0.4);
}

.stTextInput input, .stTextArea textarea, .stSelectbox select {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-primary) !important;
    border-radius: 10px !important;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(108,99,255,0.2) !important;
}

.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-secondary);
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: var(--text-secondary);
    border-radius: 8px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
}

.stTabs [aria-selected="true"] {
    background: var(--accent) !important;
    color: white !important;
}

.step-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5rem 0;
}

.tip-box {
    background: rgba(108,99,255,0.08);
    border: 1px solid rgba(108,99,255,0.25);
    border-left: 4px solid var(--accent);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin: 1rem 0;
    color: var(--text-secondary);
    font-size: 0.9rem;
}

.success-box {
    background: rgba(67,233,123,0.08);
    border: 1px solid rgba(67,233,123,0.25);
    border-left: 4px solid var(--accent3);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin: 1rem 0;
    color: #43e97b;
    font-size: 0.9rem;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    border-radius: 10px;
    margin: 4px 0;
    cursor: pointer;
    transition: all 0.2s;
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
}

.nav-item:hover, .nav-item.active {
    background: rgba(108,99,255,0.15);
    color: var(--accent);
}

label, .stMarkdown p {
    color: var(--text-secondary) !important;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
    color: var(--text-primary) !important;
}

.stExpander {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
}

.stProgress .st-bo {
    background: var(--gradient);
}

[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif;
    color: var(--accent) !important;
}
</style>
""", unsafe_allow_html=True)

# Session state init
if "profile" not in st.session_state:
    st.session_state.profile = {}
if "page" not in st.session_state:
    st.session_state.page = "home"
if "generated_resume" not in st.session_state:
    st.session_state.generated_resume = None
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0;'>
        <div style='font-family:Syne; font-size:1.5rem; font-weight:800;
             background:linear-gradient(135deg,#6c63ff,#ff6584);
             -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
            🎯 CareerCraft AI
        </div>
        <div style='color:#9090aa; font-size:0.8rem; margin-top:4px;'>Your Personal Career Assistant</div>
    </div>
    <hr style='border:none; border-top:1px solid #2a2a3e; margin:0.5rem 0 1rem;'>
    """, unsafe_allow_html=True)

    pages = {
        "🏠 Home": "home",
        "👤 My Profile": "profile",
        "📄 ATS Resume Builder": "resume",
        "🎨 Visual Templates": "templates",
        "💼 Job Application AI": "jobs",
        "💬 Interview Q&A": "qa",
        "💒 Marriage Biodata": "biodata",
        "⚙️ Settings": "settings",
    }

    for label, key in pages.items():
        is_active = st.session_state.page == key
        style = "background:rgba(108,99,255,0.15); color:#6c63ff;" if is_active else "color:#9090aa;"
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()

    st.markdown("<hr style='border:none; border-top:1px solid #2a2a3e; margin:1rem 0;'>", unsafe_allow_html=True)

    has_profile = bool(st.session_state.profile.get("name"))
    has_api = bool(st.session_state.api_key)

    st.markdown(f"""
    <div style='font-size:0.8rem; color:#9090aa;'>
        <div style='margin-bottom:6px;'>
            {'✅' if has_profile else '⭕'} Profile {'Complete' if has_profile else 'Incomplete'}
        </div>
        <div>
            {'✅' if has_api else '⭕'} AI {'Connected' if has_api else 'Not Set'}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Page routing
page = st.session_state.page

if page == "home":
    from pages import home
    home.render()
elif page == "profile":
    from pages import profile
    profile.render()
elif page == "resume":
    from pages import resume
    resume.render()
elif page == "templates":
    from pages import templates
    templates.render()
elif page == "jobs":
    from pages import jobs
    jobs.render()
elif page == "qa":
    from pages import qa
    qa.render()
elif page == "biodata":
    from pages import biodata
    biodata.render()
elif page == "settings":
    from pages import settings
    settings.render()
