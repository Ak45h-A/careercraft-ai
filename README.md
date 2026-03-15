# 🎯 CareerCraft AI — Personal Career Assistant

A powerful AI-powered web app for resumes, job applications & marriage biodata.

---

## 🚀 Quick Setup (5 minutes)

### Step 1: Install Python
Download Python 3.10+ from https://python.org

### Step 2: Install Dependencies
Open terminal/command prompt in this folder and run:
```bash
pip install -r requirements.txt
```

### Step 3: Run the App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🔑 API Key Setup
1. Go to **Settings** in the app
2. Get your free API key from https://console.anthropic.com
3. Paste it and click "Save API Key"

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 👤 Profile Manager | Store your info once, reuse everywhere |
| 📄 ATS Resume Builder | AI-tailored resumes with keyword matching |
| 📊 ATS Score Analyzer | Check your resume's ATS compatibility |
| 🎨 6 Visual Templates | Canva-style beautiful resume designs |
| 💼 Cover Letter Generator | Platform-specific cover letters |
| 🤖 Application Q&A | Auto-answers to job application questions |
| 💬 Interview Prep | Mock interviews + personalized Q&A answers |
| 💒 Marriage Biodata | 4 beautiful biodata styles |
| 📋 Application Tracker | Track all your job applications |
| 📥 Multi-format Export | PDF (via HTML), DOCX, HTML |

## 📤 Export Options
- **HTML** → Open in Chrome → Ctrl+P → Save as PDF (best quality)
- **DOCX** → Edit in Microsoft Word / Google Docs
- **TXT** → Plain text for pasting anywhere

## 🆓 Free Alternative (No API Key Needed)
Use Ollama with a local AI model:
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download a model
ollama pull llama3

# The app can be configured to use localhost
```

---
Built with ❤️ using Streamlit + Anthropic Claude
